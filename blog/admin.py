from django.contrib import admin
from mediumeditor.admin import MediumEditorAdmin
from blog.models import Post

class PostAdmin(MediumEditorAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title')}
    mediumeditor_fields = ('text')

admin.site.register(Post, PostAdmin)
