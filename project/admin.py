from django.contrib import admin
from mediumeditor.admin import MediumEditorAdmin
from project.models import Project, Tech

# Add, edit and delete projects from the admin
class ProjectAdmin(MediumEditorAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    mediumeditor_fields = ('description')

# Register Project and ProjectAdmin to the admin
admin.site.register(Project, ProjectAdmin)

# Register Tech to the admin
admin.site.register(Tech)

