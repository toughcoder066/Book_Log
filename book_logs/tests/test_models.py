from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Topic, Entry

class TopicModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.topic = Topic.objects.create(title='Test Topic', owner=self.user)

    def test_topic_str(self):
        self.assertEqual(str(self.topic), 'Test Topic')

    def test_topic_title(self):
        self.assertEqual(self.topic.title, 'Test Topic')

    def test_topic_owner(self):
        self.assertEqual(self.topic.owner, self.user)


class EntryModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.topic = Topic.objects.create(title='Test Topic', owner=self.user)
        self.entry = Entry.objects.create(topic=self.topic, entry='Test Entry')

    def test_entry_str(self):
        self.assertEqual(str(self.entry), 'Test Entry ...')

    def test_entry_topic(self):
        self.assertEqual(self.entry.topic, self.topic)

    def test_entry_entry(self):
        self.assertEqual(self.entry.entry, 'Test Entry')
