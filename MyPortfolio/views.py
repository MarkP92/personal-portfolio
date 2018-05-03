from django.views.generic import TemplateView, ListView
from django.utils import timezone
from blog.models import Post
from project.models import Project
from contact.forms import ContactForm

class HomePage(ListView):
    template_name = 'index.html'
    context_object_name = 'post_list'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context.update({'post_list' : Post.objects.filter(published_at__lte=timezone.now()).order_by('-created_at')[:3], 'project_list' : Project.objects.order_by('-created_at')[:3], 'contact_form' : ContactForm})
        return context