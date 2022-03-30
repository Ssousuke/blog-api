from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('post/list/', views.BlogListPosts.as_view(), name='list_post'),
    path('post/detail/<int:pk>/', views.BlogGetPost.as_view(), name='get_post'),
    path('list/categories/', views.BlogListCategory.as_view(),
         name='list_categories'),
]
