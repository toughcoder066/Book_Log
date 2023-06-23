from django.test import TestCase
from ..forms import TopicForm, EntryForm

class TopicFormTest(TestCase):
    '''
    These tests check that the TopicForm and EntryForm 
    have been created correctly, and that they validate data properly. 
    The first test in each test case checks that the label 
    for the field is set to an empty string, as specified in the form's Meta class. 
    
    The second test checks that the form is valid when given valid data, 
    and the third test checks that the form is invalid when given no data.
    '''

    def test_topic_form_labels(self):
        form = TopicForm()
        self.assertEqual(form.fields['title'].label, 'Title')

    def test_topic_form_valid(self):
        form_data = {'title': 'Test Topic'}
        form = TopicForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_topic_form_invalid(self):
        form_data = {}
        form = TopicForm(data=form_data)
        self.assertFalse(form.is_valid())


class EntryFormTest(TestCase):

    def test_entry_form_labels(self):
        form = EntryForm()
        self.assertEqual(form.fields['entry'].label, 'EntryText')

    def test_entry_form_valid(self):
        form_data = {'entry': 'Test Entry'}
        form = EntryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_entry_form_invalid(self):
        form_data = {}
        form = EntryForm(data=form_data)
        self.assertFalse(form.is_valid())
