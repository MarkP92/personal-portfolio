from django import forms
from django.forms import ModelForm
from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        # Widgets / Classes for CSS
        widgets = {'title':forms.TextInput(attrs={'class':'textinputclass'}), 'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})}