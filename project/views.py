from django.shortcuts import render
from django.views.generic import ListView, DetailView
from project.models import Project
from django.utils import timezone

# List view of projects
class ProjectListView(ListView):
    model = Project
    
    # Queryset; all projects
    def get_queryset(self):
        return Project.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')

# Detailed view of Project
class ProjectDetailView(DetailView):
    model = Project
