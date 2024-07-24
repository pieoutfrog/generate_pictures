from django import forms


class AchievementForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Имя и Фамилия")
    achievement_text = forms.CharField(widget=forms.Textarea, label="Текст достижения")
    template_id = forms.IntegerField(widget=forms.HiddenInput)