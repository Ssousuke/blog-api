from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Post
from .serializers import BlogPostSerializer, BlogCategorySerializer


class BlogGetPost(APIView):
    """
    Uma visualização que permite uma solicitação GET para um artigo de notícias no banco de dados
    """

    def get(self, request, pk, format=None):
        try:
            post = Post.objects.get(published=True, pk=pk)
            serializer = BlogPostSerializer(post)
            return Response(serializer.data, status.HTTP_200_OK)
        except Post.DoesNotExist:   
            return Response(status=status.HTTP_404_NOT_FOUND)


class BlogListPosts(generics.ListAPIView):
    """
    Uma visualização que permite uma solicitação GET para a listagem de postagens no banco de dados
    """
    queryset = Post.objects.filter(published=True)
    serializer_class = BlogPostSerializer
    

class BlogListCategory(generics.ListAPIView):
    """
    Uma visualização que permite uma solicitação GET para uma lista de categorias no banco de dados
    """
    queryset = Category.objects.all()
    serializer_class = BlogCategorySerializer
