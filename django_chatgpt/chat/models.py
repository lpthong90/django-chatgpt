from django.db import models
from django.conf import settings


class MessageManager(models.Manager):
    def last_many(self, n):
        messages = self.order_by('-id')[:n]
        messages = sorted(list(messages), key=lambda m: m.id)
        return messages


class Chat(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chats')

    @property
    def name(self):
        return f"Chat {self.id}"

    def __str__(self):
        return self.title


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    USER = 'user'
    BOT = 'bot'
    SYSTEM = 'system'
    ROLE_CHOICES = [
        (USER, 'User'),
        (BOT, 'Bot'),
        (SYSTEM, 'System'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)

    objects = MessageManager()

    def __str__(self):
        return f"Message from {self.chat.title} at {self.timestamp}"

    @property
    def openai_message(self):
        return {'role': self.role, 'content': self.content}
