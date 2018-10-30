from django.contrib import admin
from project.models import Project, Tech

# Add, edit and delete projects from the admin
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register Project and ProjectAdmin to the admin
admin.site.register(Project, ProjectAdmin)

# Register Tech to the admin
admin.site.register(Tech)

