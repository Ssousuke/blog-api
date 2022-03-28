from rest_framework import generics
from .models import Post, Category
from .serializers import BlogPostSerializer, BlogCategorySerializer


class BlogPostApiView(generics.ListCreateAPIView):
    queryset = Post.objects.filter(published=True)
    serializer_class = BlogPostSerializer
