from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
import PIL

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategorier'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug, 'pk':self.pk})

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now) 
    published_at = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='img', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Indlæg'
        verbose_name_plural = 'Indlæg'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug, 'pk':self.pk})

    def __str__(self):
        return self.title