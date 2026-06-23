from django.urls import path
from .views import create_post, get_posts, get_post, update_post, delete_post

urlpatterns = [
    path('create/', create_post),
    path('posts/', get_posts),
    path('posts/<int:id>/', get_post),
    path('update/<int:id>/', update_post),
    path('delete/<int:id>/', delete_post),
]