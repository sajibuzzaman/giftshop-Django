from django.contrib import admin
from .models import Setting, Slider, About, Team, ContactMessage

# Register your models here.
admin.site.register(Setting)
admin.site.register(Slider)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(ContactMessage)
