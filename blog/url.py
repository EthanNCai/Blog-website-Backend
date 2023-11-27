from django.urls import path

from . import views

urlpatterns = [
    path("blogFlow", views.blogFlow, name="blogFlow"),
    path('blog-avatar/<int:id>/', views.blogAvatar, name='blog_avatar'),
    path('blog-article/<int:id>/', views.blogArticle, name='blog_article'),
    path('blog_find_id/<int:id>/', views.blog_find_id, name='blog_find_id'),
]


# blog_find_id