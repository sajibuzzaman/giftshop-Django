from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = RichTextUploadingField()
    address = RichTextUploadingField()
    phone = models.IntegerField()
    fax = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=50)
    smptserver = models.CharField(max_length=100)
    smtpemail = models.EmailField(blank=True, null=True, max_length=50)
    smptpassword = models.CharField(blank=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=100)
    logo = models.ImageField(blank=True, null=True, upload_to='icon/')
    favicon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.URLField(blank=True, max_length=50)
    instagram = models.URLField(blank=True, max_length=50)
    twitter = models.URLField(blank=True, max_length=50)
    pinterest = models.URLField(blank=True, max_length=50)
    linkedin = models.URLField(blank=True, max_length=50)
    aboutus = RichTextUploadingField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title