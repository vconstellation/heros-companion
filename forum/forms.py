from django import forms
from .models import Thread, Post

class ThreadCreateForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Thread
        fields = ['subject', 'message']

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']