from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display=['user','country','image_tag']
	list_filter=['user',]
  
# Register your models here.

