from django.contrib import admin
from mediumeditor.admin import MediumEditorAdmin
from project.models import Project

class ProjectAdmin(MediumEditorAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    mediumeditor_fields = ('description')

admin.site.register(Project, ProjectAdmin)
