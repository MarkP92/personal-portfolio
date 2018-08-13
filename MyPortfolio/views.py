from django.views.generic import TemplateView, ListView
from django.utils import timezone
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from blog.models import Post
from project.models import Project
from contact.forms import ContactForm

# View for the index - listview of projects and posts
class HomePage(ListView):
    template_name = 'index.html'
    context_object_name = 'post_list'
    model = Post

    # Get the data; posts and projects
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context.update({'post_list' : Post.objects.filter(published_at__lte=timezone.now()).order_by('-created_at')[:3], 'project_list' : Project.objects.order_by('-created_at')[:3], 'contact_form' : ContactForm})
        return context

# Custom page for 404
def not_found(request, exception):
    return render(request, '404.html')

# Custom page for 500
def server_error(request):
    return render(request, '500.html')