from django.contrib import admin
from .models import Setting, Slider, About, Team, ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'email', 'message', 'ip']
    list_display = ['name', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    list_per_page = 10

# Register your models here.
admin.site.register(Setting)
admin.site.register(Slider)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(ContactMessage, ContactMessageAdmin)
