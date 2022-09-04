from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework import exceptions


class Message(models.Model):
    """Модель сообщения. Отправитель (модель User) берется из
    системы аутентификации Django"""
    sender = models.ForeignKey(
        User,
        verbose_name='Отправитель',
        related_name='messages',
        on_delete=models.CASCADE,
    )
    message = models.TextField('Текст')
    received_at = models.DateTimeField('Получено в', auto_now=True)


class BearerTokenAuthentication(TokenAuthentication):
    """Переопределение класса TokenAuthentication для приведения префикса
    токена к виду 'Bearer_' """
    keyword = 'Bearer'

    def authenticate(self, request):
        auth = get_authorization_header(request).split('_'.encode())

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)
