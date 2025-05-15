from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView, PostCreateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    #path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), # user posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # base on primary key
    path('post/new/', PostCreateView.as_view(), name='post-create'), # create new post
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), # delete post
    path('about/', views.about, name='blog-about'),
]
