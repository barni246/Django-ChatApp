from django.test import TestCase
from chat.models import Chat, Message
from django.contrib.auth.models import User
from django.utils import timezone


class MessageTestCase(TestCase):
    def setUp(self):
        self.chat = Chat.objects.create() 
        self.user = User.objects.create(username='testuser')  

    def test_message_creation(self):
        message = Message.objects.create(
            text='Test-Nachricht',
            chat=self.chat,
            author=self.user,
            receiver=self.user,
            created_at=timezone.now() 
        )

        self.assertEqual(message.text, 'Test-Nachricht')
        self.assertEqual(message.chat, self.chat)
        self.assertEqual(message.author, self.user)
        self.assertEqual(message.receiver, self.user)
        self.assertIsNotNone(message.created_at) 
