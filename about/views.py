from django.shortcuts import render
from django.views.generic import TemplateView

# Simple TemplateView for About Page
class AboutView(TemplateView):
    template_name = 'about/about.html'