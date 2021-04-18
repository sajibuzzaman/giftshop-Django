from django.contrib import admin
from .models import Blog, CommentBlog


class CommentBlogInline(admin.TabularInline):
    model = CommentBlog
    extra = 0
    readonly_fields = ['blog','user', 'comment', 'ip']
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted', 'image_tag']
    list_filter = ['date_posted']
    inlines = [CommentBlogInline] 
    list_per_page = 10


class CommentBlogAdmin(admin.ModelAdmin):
    readonly_fields = ['blog','user', 'comment', 'ip']
    list_display = ['blog', 'status', 'created_at', 'updated_at', 'user']
    list_filter = ['status', 'created_at']
    list_per_page = 10

# Register your models here.
admin.site.register(Blog, BlogAdmin)
