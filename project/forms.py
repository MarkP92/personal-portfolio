from django import forms
from django.forms import ModelForm
from mediumeditor.widgets import MediumEditorTextarea
from project.models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        # Widgets / Classes for CSS
        widgets = {'description' : MediumEditorTextarea(),}