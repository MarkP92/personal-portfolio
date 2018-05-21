from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post, Category
from django.utils import timezone


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    
    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super(PostListView , self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('title')
        return context

class PostDetailView(DetailView):
    model = Post

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'

class AllCategoriesView(ListView):
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        return Category.objects.all()


