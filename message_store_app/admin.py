from django.contrib import admin

from message_store_app.models import Message


@admin.register(Message)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['sender', 'received_at', 'message']
