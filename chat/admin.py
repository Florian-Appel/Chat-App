from django.contrib import admin
from django.contrib import admin
from .models import Chat, Message

class MessageAdmin(admin.ModelAdmin):
    """
    Here you can set what and how it should be displayed on the admin page.
    """
    fields = ('chat', 'text', 'chreated_at', 'author', 'receiver') # Anzeige in der Detailansicht
    list_display = ('chat','chreated_at', 'author', 'text', 'receiver') # Anzeige in der Übersicht
    search_fields = ('text',) # Suchfeld

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)