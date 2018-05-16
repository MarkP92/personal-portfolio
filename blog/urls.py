from django.urls import path, re_path
from blog import views

# app_name = 'blog' 

urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    re_path(r'^indlæg/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name="post_detail"),
    path('kategorier/', views.AllCategoriesView.as_view(), name="category_list"),
    re_path(r'^kategorier/(?P<slug>[-\w]+)/$', views.CategoryDetailView.as_view(), name="category_detail"),
]