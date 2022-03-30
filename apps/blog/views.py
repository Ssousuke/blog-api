from django.http import Http404
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Category
from .serializers import BlogPostSerializer, BlogCategorySerializer


class BlogGetPost(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = BlogPostSerializer(post)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogListPosts(generics.ListAPIView):
    queryset = Post.objects.filter(published=True)
    serializer_class = BlogPostSerializer
