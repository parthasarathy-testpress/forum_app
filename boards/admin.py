from django.contrib import admin
from .models import Board, Topic, Post

# Inline for posts in topic admin
class PostInline(admin.TabularInline):
    model = Post
    extra = 1  # number of empty forms to display
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'board', 'starter', 'last_updated')
    list_filter = ('board', 'last_updated')
    search_fields = ('subject', 'starter__username')
    inlines = [PostInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_by', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('message', 'created_by__username', 'updated_by__username')
    readonly_fields = ('created_at', 'updated_at')
