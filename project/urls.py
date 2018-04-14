from django.urls import path, re_path
from project import views

# app_name = 'project'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name="project_list"),
    re_path(r'^(?P<slug>[-\w]+)/$', views.ProjectDetailView.as_view(), name="project_detail"),
]