from .models import article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class articleForm(ModelForm):
    class Meta:
        model = article
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название новости'
            }),
            "anons": TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Анонс новости'
            }),
            "data": DateTimeInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs = {
                'class': 'form-control',
                'placeholder': 'Текст новости'
            })
        }