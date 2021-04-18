from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm
from django.utils.safestring import mark_safe


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
    smptserver = models.CharField(blank=True, max_length=100)
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

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.logo.url))
    image_tag.short_description = 'Logo'

class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='slider/')
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'
class About(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to = "image/")
    video_link = models.URLField(blank=True, max_length=50)
    happy_clients = models.PositiveIntegerField(default=0)
    award_wining = models.PositiveIntegerField(default=0)
    project_done = models.PositiveIntegerField(default=0)
    event = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="team/", default= 'default.jpg')

    def __str__(self):
       return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.picture.url))
    image_tag.short_description = 'Picture'

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),

    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    message = models.TextField(max_length=1000, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    ip = models.CharField(max_length=100, blank=True)
    Note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']