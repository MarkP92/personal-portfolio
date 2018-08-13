from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post, Category
from django.utils import timezone

# List of Posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    
    # Queryset for the list
    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')

    # Get the context
    def get_context_data(self, **kwargs):
        context = super(PostListView , self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('title')
        return context

# Detailed view for specific Post
class PostDetailView(DetailView):
    model = Post

# Detailed view for specific Category
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'

# List view of all the categories
class AllCategoriesView(ListView):
    template_name = 'blog/category_list.html'

    # Queryset
    def get_queryset(self):
        return Category.objects.all()


