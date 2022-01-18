from django import forms

from .models import Topics

class TopicForm(forms.ModelForm):
  class Meta:
    model = Topic
    fields = ['text']
    labels = {'text': ''}
