from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
import PIL

# Model for Tech (ManyToMany)
class Tech(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Teknologi'
        verbose_name_plural = 'Teknologier'

    def __str__(self):
        return self.title

# Model for Project
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech = models.ManyToManyField(Tech)
    image = models.ImageField(upload_to='../media/img', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.URLField(max_length=120, default='', blank=True, null=True)
    github = models.URLField(max_length=120, default='', blank=True, null=True)
    slug = models.SlugField(default='')
    seo_desc = models.CharField(max_length=120, default='Portfolio og personlig hjemmeside for Mark Petersen', blank=True, null=True)

    # Meta
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Projekt'
        verbose_name_plural = 'Projekter'

    # Slugify the title when saved
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # Find object with correct slug / id
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug':self.slug,'pk':self.pk})

    # Return title as string
    def __str__(self):
        return self.title
