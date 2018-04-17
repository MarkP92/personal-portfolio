from django.views.generic import TemplateView, ListView
from blog.models import Post
        
class HomePage(TemplateView):
    template_name = 'index.html'