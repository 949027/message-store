from django.db import models
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        verbose_name='Отправитель',
        related_name='messages',
        on_delete=models.CASCADE,
    )
    message = models.TextField('Текст')
    received_at = models.DateTimeField('Получено в', auto_now=True)


class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer_'
