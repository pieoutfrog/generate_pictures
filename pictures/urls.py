from django.urls import path
from .views import generate_achievement


app_name = 'pictures'


urlpatterns = [
    path('generate/', generate_achievement, name='generate_achievement'),
]