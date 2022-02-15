from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'posted_by', 'created']
    list_display_links = ['title']
    list_per_page = 40 
    search_fields = ('title', 'posted_by',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'blog', 'posted_by', 'created']
    list_display_links = ['description']
    list_per_page = 40 
    search_fields = ('description', 'posted_by',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)