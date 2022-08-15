from datetime import date
from email.policy import default
from django.db import models
from django.conf import settings

class Chat(models.Model):
    chreated_at = models.DateField(default=date.today)

class Message(models.Model):
    text = models.CharField(max_length=500)
    chreated_at = models.DateField(default=date.today)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True) # Die letzten 3: Standartwert ist nichts, wir dürfen nichts reingeben und die Datenbank akzeptiert nichts. 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')