from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogListPosts.as_view(), name='list_post'),
    path('detail/<int:pk>/', views.BlogGetPost.as_view(), name='get_post'),
    path('new/<int:pk>/', views.BlogListPosts.as_view(), name='new_post'),
    path('delete/<int:pk>/', views.BlogListPosts.as_view(), name='delete_post'),
]
