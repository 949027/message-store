import re
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from message_store_app.models import Message


class MessageSerializer(ModelSerializer):
    """Сериалайзер для поступающих сообщений"""
    class Meta:
        model = Message
        fields = ['message']


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def process_request(request):
    """Логика эндпоинта `/app/message`.
    1) Полученные данные проходят через сериалайзер.
    2) Если полученное сообщение соответствует паттерну "history {amount},
    тогда формируется и отправляется список последних сообщений этого пользователя.
    3) Если сообщение не соответствует паттерну, то оно сохраняется в БД
    и отправляется сообщение 'Message saved'"""
    serializer = MessageSerializer(data=request.data)
    serializer.is_valid(raise_exception=False)
    message = serializer.validated_data['message']

    if re.fullmatch(r'history \d+', message):
        message_amount = int(message.split(' ')[1])
        messages = list(Message.objects
                        .filter(sender=request.user)
                        .order_by('-received_at')[:message_amount]
                        .values()
                        )
        return Response(messages)

    Message.objects.create(
        sender=request.user,
        message=serializer.validated_data['message']
    )
    return Response({'message': 'Message saved'})
