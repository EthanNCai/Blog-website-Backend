from django.urls import path

from . import views

urlpatterns = [
    path("blog_flow", views.blogFlow, name="blogFlow"),
    path('blog-avatar/<int:id>/', views.blogAvatar, name='blog_avatar'),
    path('blog-article/<int:id>/', views.blogArticle, name='blog_article'),
    path('blog_find_id/<int:id>/', views.blog_find_id, name='blog_find_id'),
    path('blog_likes_increase/<int:id>/', views.blog_likes_increase, name='blog_likes_increase'),
    path('blog_likes_decrease/<int:id>/', views.blog_likes_decrease, name='blog_likes_decrease'),
    path('blog_hates_increase/<int:id>/', views.blog_hates_increase, name='blog_hates_increase'),
    path('blog_hates_decrease/<int:id>/', views.blog_hates_decrease, name='blog_hates_decrease'),
    path('blog_flow_by_keyword/<str:keyword>/', views.blog_flow_by_keyword, name='blog_flow_by_keyword'),
]


# blog_find_id