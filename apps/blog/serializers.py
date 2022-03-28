from rest_framework import serializers
from .models import Post, Category


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'created_at',
            'updated_at',
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'body',
            'thumb',
            'category',
            'author',
            'created_at',
            'updated_at',
            'published',
        ]
