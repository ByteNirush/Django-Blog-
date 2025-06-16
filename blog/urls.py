from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteview,
    about, 
    UserPostListView
)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # <-- Add this line
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # <-- Add this line
    path('post/<int:pk>/delete/', PostDeleteview.as_view(), name='post-delete'),  # <-- Add this line
    path('about/', about, name='blog-about'),
]

