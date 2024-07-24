from django.contrib import admin
from .models import AchievementTemplate


@admin.register(AchievementTemplate)
class AchievementTemplateAdmin(admin.ModelAdmin):
    list_display = ('sport', 'title', 'is_available')
    search_fields = ('sport', 'title')



