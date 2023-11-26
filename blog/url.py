from django.urls import path

from . import views

urlpatterns = [
    path("blogFlow", views.blogFlow, name="blogFlow"),
    path('blog-avatar/<int:id>/', views.blogAvatar, name='blog_avatar'),
]