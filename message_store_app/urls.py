from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from message_store_app.views import process_request

#from .views import create_token

urlpatterns = [
    path('token/', obtain_auth_token, name='obtain_auth_token'),
    path('message/', process_request, name='process_request'),
]
