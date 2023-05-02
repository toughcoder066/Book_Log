from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
        labels = {'title':'Title'}
        help_texts = {
           'title': ('enter your topic here.'),
        }
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['entry']
        labels = {'entry':'EntryText'}
        #help_texts = {
        #    'entry': ('enter your text here.'),
        #}
        widgets = {'entry':forms.Textarea(attrs={'cols': 80, 'rows': 20})}