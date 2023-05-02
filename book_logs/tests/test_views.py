from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Topic,Entry



class TestViews(TestCase):
    
    #These tests use the Django test
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.topic = Topic.objects.create(title='Test Topic', owner=self.user)
        self.entry = Entry.objects.create(topic=self.topic, entry='Test EntryText')

    def test_index_view(self):
        url = reverse('book_logs:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_logs/index.html')

    def test_topics_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_logs:topics')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_logs/topics.html')

    def test_topic_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_logs:topic', args=[self.topic.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_logs/topic.html')

    def test_add_topic_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_logs:add_topic')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_logs/add_topic.html')

        data = {'title': 'New Topic'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('book_logs:topics'))

    def test_add_entry_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_logs:add_entry', args=[self.topic.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_logs/add_entry.html')

        data = {'entry': 'New EntryText'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('book_logs:topic', args=[self.topic.id]))

    def test_edit_entry_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_logs:edit_entry', args=[self.entry.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_logs/edit_entry.html')

        data = {'entry': 'New EntryText'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('book_logs:topic', args=[self.topic.id]))

    def test_delete_entry_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book_logs:delete_entry', args=[self.entry.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('book_logs:topic', args=[self.topic.id]))
