from django.urls import path, re_path
from blog import views

# app_name = 'blog' 

urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    re_path(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name="post_detail"),
]