from django.urls import path
from . import views              # . is used for current directory
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'Post-details'),
    path('post/new/', PostCreateView.as_view(), name = 'New-Post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'Post-Update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'Post-Delete')
]
