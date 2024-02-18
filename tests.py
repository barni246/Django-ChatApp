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
        
# python manage.py test --verbosity=2 oder 3


# alabaster==0.7.16
# asgiref==3.7.2
# Babel==2.14.0
# certifi==2024.2.2
# charset-normalizer==3.3.2
# colorama==0.4.6
# Django==5.0.2
# docutils==0.20.1
# idna==3.6
# imagesize==1.4.1
# Jinja2==3.1.3
# MarkupSafe==2.1.5
# packaging==23.2
# Pygments==2.17.2
# requests==2.31.0
# snowballstemmer==2.2.0
# Sphinx==7.2.6
# sphinx-rtd-theme==2.0.0
# sphinxcontrib-applehelp==1.0.8
# sphinxcontrib-devhelp==1.0.6
# sphinxcontrib-htmlhelp==2.0.5
# sphinxcontrib-jquery==4.1
# sphinxcontrib-jsmath==1.0.1
# sphinxcontrib-qthelp==1.0.7
# sphinxcontrib-serializinghtml==1.1.10
# sqlparse==0.4.4
# tzdata==2024.1
# urllib3==2.2.0

