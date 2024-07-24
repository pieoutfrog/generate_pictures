from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import AchievementTemplate
from .forms import AchievementForm
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64


def generate_image(template, full_name, achievement_text):
    # Загрузка изображения шаблона
    base_image = Image.open(template.template_image)
    draw = ImageDraw.Draw(base_image)

    # Установка шрифта и размера
    font = ImageFont.truetype("static/Arial.ttf", 36)

    # Добавление текста на изображение
    draw.text((50, 50), full_name, font=font, fill="black")  # координаты для имени
    draw.text((50, 150), achievement_text, font=font, fill="black")  # координаты для достижения

    # Сохранение изображения в памяти
    buffer = BytesIO()
    base_image.save(buffer, format='PNG')
    return buffer.getvalue()


def generate_achievement(request):
    if request.method == "POST":
        form = AchievementForm(request.POST)
        if form.is_valid():
            template = get_object_or_404(AchievementTemplate, id=form.cleaned_data['template_id'])
            image_data = generate_image(template, form.cleaned_data['full_name'], form.cleaned_data['achievement_text'])

            response = HttpResponse(image_data, content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="achievement.png"'
            return response
    else:
        form = AchievementForm()

    templates = AchievementTemplate.objects.filter(is_available=True)
    return render(request, 'generate_achievement.html', {'form': form, 'templates': templates})
