from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', views.LogoutAPI.as_view(), name='logout'),
    path('user/', views.UserAPI.as_view(), name='user'),
    
    # Profile
    path('profile/', views.ProfileAPI.as_view(), name='profile'),
    
    # Posts
    path('posts/', views.PostListCreateAPI.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailAPI.as_view(), name='post-detail'),
    
    # Likes
    path('posts/<int:post_id>/like/', views.LikeAPI.as_view(), name='like'),
    
    # Comments
    path('posts/<int:post_id>/comments/', views.CommentListCreateAPI.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetailAPI.as_view(), name='comment-detail'),
]