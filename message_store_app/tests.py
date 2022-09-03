import requests
from django.contrib.auth.models import User
from django.test import TestCase


class ModelsTestCase(TestCase):
    pass


# class ViewsTestCase(TestCase):
#     def test_index_loads_properly(self):
#         username = 'test_user'
#         password = 'Qq123456'
#
#         user = User.objects.create(username=username, password=password)
#
#         url = f'http://127.0.0.1:8000/app/token/'
#         json = {
#             'username': 'qwerty123',
#             'password': 'Qq367077',
#         }
#         response = requests.post(url, json=json)
#
#         response.raise_for_status()
#
#         response = self.client.post('http://127.0.0.1:8000/app/message/', headers=headers, json=json)
#         self.assertEqual(response.status_code, 200)
