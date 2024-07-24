from django.db import models


class AchievementTemplate(models.Model):
    objects = models.Manager()
    sport = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    template_image = models.ImageField(upload_to='templates/')
    text_area_name = models.CharField(max_length=100)
    text_area_description = models.CharField(max_length=100)
