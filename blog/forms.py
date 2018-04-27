'''
from django import forms
from django.forms import ModelForm
from mediumeditor.widgets import MediumEditorTextarea
from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        # Widgets / Classes for CSS
        widgets = {'text' : MediumEditorTextarea(),}
'''