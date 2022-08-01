from typing import Dict, Sequence
from django.contrib import admin
from .models import Category, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_available', 'author')
    list_filter = ('is_available',)
    search_fields: Sequence[str] = ('title', 'content')
    readonly_fields: Sequence[str] = ('slug', 'last_update',)
    # prepopulated_fields: Dict[str, Sequence[str]] = {'slug':('title',)}
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('slug', )
    list_display = ('name', 'slug')
    