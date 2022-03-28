from csv import list_dialects
from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'created_at',
        'updated_at',
        'published'
    ]
    list_display_links = [
        'title',
        'description',
        'created_at',
        'updated_at',
    ]
    list_editable = [
        'published'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'created_at',
        'updated_at',
    ]
    list_display_links = [
        'id',
        'name',
        'created_at',
        'updated_at',
    ]
