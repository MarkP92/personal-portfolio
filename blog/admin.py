from django.contrib import admin
from mediumeditor.admin import MediumEditorAdmin
from blog.models import Post, Category

class PostAdmin(MediumEditorAdmin, admin.ModelAdmin):
    list_filter = ('title', 'category')
    search_fields = ('title', 'text', 'category')
    prepopulated_fields = {'slug': ('title',)}
    mediumeditor_fields = ('text')

admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
