from django.contrib import admin
from mediumeditor.admin import MediumEditorAdmin
from blog.models import Post, Category

# PostAdmin - create, edit and delete posts from admin
class PostAdmin(MediumEditorAdmin, admin.ModelAdmin):
    list_filter = ('title', 'category')
    search_fields = ('title', 'text', 'category')
    prepopulated_fields = {'slug': ('title',)}
    mediumeditor_fields = ('text')

# Register Post and PostAdmin to the admin
admin.site.register(Post, PostAdmin)

# CategoryAdmin - create, edit and delete categories from admin
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

# Register Cateory and CategoryAdmin to the admin
admin.site.register(Category, CategoryAdmin)
