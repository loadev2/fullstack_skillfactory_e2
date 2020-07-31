from django.contrib import admin
from common.models import  Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass