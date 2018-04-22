from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
import PIL

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now) 
    published_at = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(default='')
    image = models.ImageField(upload_to='img', null=True, blank=True)

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