from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import BlogPostSerializer


class BlogGetPost(APIView):
    def get(self, request, pk, format=None):
        try:
            post = Post.objects.get(published=True, pk=pk)
            serializer = BlogPostSerializer(post)
            return Response(serializer.data, status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            post = Post.objects.get(published=True, pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class BlogListPosts(generics.ListAPIView):
    """
    API de listagem de postagens
    """
    queryset = Post.objects.filter(published=True)
    serializer_class = BlogPostSerializer
