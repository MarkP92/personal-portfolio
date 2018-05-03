from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post
from project.models import Project
 
class StaticSiteMap(Sitemap):
 
    def items(self):
        return [
            'home',
            'about',
            'contact',
            'send',
            'project_list',
            'post_list',
        ]
 
    def location(self, item):
        return reverse(item)

class PostSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.published_at

    def location(self, item):
        return reverse('post_detail', args=[item.slug])

class ProjectSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, item):
        return reverse('project_detail', args=[item.slug])
    