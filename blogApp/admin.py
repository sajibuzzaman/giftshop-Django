from django.contrib import admin
from .models import Blog, CommentBlog


class CommentBlogAdmin(admin.ModelAdmin):
    readonly_fields = ['blog','user', 'comment', 'ip']
    list_display = ['blog', 'status', 'created_at', 'updated_at', 'user']
    list_filter = ['status', 'created_at']
    list_per_page = 10

# Register your models here.
admin.site.register(Blog)
admin.site.register(CommentBlog, CommentBlogAdmin)