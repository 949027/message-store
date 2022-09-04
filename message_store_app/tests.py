import requests
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


client = APIClient()


class ViewsTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user',
                                                         password='test1234',
                                                         email='test@example.com')

    def test_sending_token(self):
        data = {'username': 'test_user', 'password': 'test1234'}
        response = client.post(reverse('obtain_auth_token'), data, format='json')
        token = response.data['token']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(token), 40)

    def test_receiving_message(self):
        data = {'message': 'hello'}
        client.force_authenticate(user=self.user)
        response = client.post(reverse('process_request'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Message saved')

    def test_sending_history(self):
        client.force_authenticate(user=self.user)
        for _ in range(10):
            data = {'message': 'hello'}
            client.post(reverse('process_request'), data, format='json')
        data = {'message': 'history 5'}
        response = client.post(reverse('process_request'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
