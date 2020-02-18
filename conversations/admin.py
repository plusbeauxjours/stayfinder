from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Definition"""

    list_display = ("__str__", "created_at")


@admin.register(models.Conversation)
class ConversatinoAdmin(admin.ModelAdmin):

    """Conversation Admin Definition"""

    list_display = ("__str__", "count_messages", "count_participants")
