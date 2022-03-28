from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [
    path('list/', views.BlogPostApiView.as_view(), name='list_post'),
]
