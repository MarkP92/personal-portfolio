from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostForm
from django.urls import reverse_lazy
from django.utils import timezone


class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')

class PostDetailView(DetailView):
    model = Post