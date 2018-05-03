from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
import PIL

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech = models.CharField(max_length=150, default='', blank=True, null=True)
    image = models.ImageField(upload_to='../media/img', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.URLField(max_length=120, default='', blank=True, null=True)
    github = models.URLField(max_length=120, default='', blank=True, null=True)
    slug = models.SlugField(default='')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Projekt'
        verbose_name_plural = 'Projekter'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug':self.slug,'pk':self.pk})

    def __str__(self):
        return self.title