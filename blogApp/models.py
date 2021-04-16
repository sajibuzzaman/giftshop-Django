from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='blog/')
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class CommentBlog(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),

    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=True)
    ip = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='True')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentFormBlog(ModelForm):
    class Meta:
        model = CommentBlog
        fields = ['comment']