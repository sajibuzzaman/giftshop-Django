from django.contrib import admin
from .models import Setting, Slider, About, Team, ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'email', 'message', 'ip']
    list_display = ['name', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    list_per_page = 10

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'happy_clients', 'award_wining', 'project_done', 'event', 'status']
    list_editable = ['happy_clients', 'award_wining', 'project_done', 'event']

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status']
    list_editable = ['status']
    fieldsets = [
        ('Website Details' , {'fields': ['title', 'keyword', 'description', 'address', 'phone', 'fax', 'email', 'logo', 'favicon', 'aboutus', 'reference', 'status']}),
        ('SMPT Details' , {'fields': ['smptserver', 'smtpemail', 'smptpassword', 'smptport'], 'classes': ['collapse']}),
        ('Social Network Link', {'fields': ['facebook', 'instagram', 'twitter', 'pinterest', 'linkedin'], 'classes': ['collapse']}),
    ]

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'default']
    list_editable = ['default']
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'image_tag']
    list_editable = ['position']

# Register your models here.
admin.site.register(Setting, SettingAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
