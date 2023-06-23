from django.test import TestCase
#from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class TestUsersViews(TestCase):
    
    def test_register_view(self):
        url = reverse('users:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

        data = {'username': 'testcaseuser','password1':'@tcpassword','password2':'@tcpassword','email':'test@email.com'}
        response = self.client.post(url, data)
        #response = self.client.login(username='testuser', password='testpass', email='test@email.com')
        #print(response.content)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,reverse('book_logs:index'))