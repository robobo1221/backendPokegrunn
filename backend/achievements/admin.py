from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Business, Achievement

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'category', 'langitude', 'longitude', 'created_at', 'updated_at')
    search_fields = ['name']
    readonly_fields = ['code', 'qrcode']

admin.site.register(Business)
admin.site.register(Achievement, AchievementAdmin)