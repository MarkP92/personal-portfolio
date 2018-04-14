from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from project.models import Project
from django.utils import timezone

class ProjectListView(ListView):
    model = Project
    
    def get_queryset(self):
        return Project.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')

class ProjectDetailView(DetailView):
    model = Project
