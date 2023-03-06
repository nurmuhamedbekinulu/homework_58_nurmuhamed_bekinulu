from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Task
from django.core.validators import MinLengthValidator, BaseValidator
from datetime import datetime


class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value):
        message = 'Максимальная длина заголовка %(limit_value)s. Выввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value > limit_value

    def clean(self, value):
        return len(value)


class CustomDateValidator(BaseValidator):
    message = 'Введите дату в формате гггг-мм-дд'

    def __init__(self, limit_value=None):
        super().__init__(limit_value)

    def __call__(self, value=None):
        if value and value.strip():
            try:
                datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                raise ValidationError(self.message, code=self.code)


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        validators=(MinLengthValidator(limit_value=2, message='Минимальная длина 2 символа'), CustomLenValidator(20)))
    description = forms.CharField(
        max_length=3000,
        validators=(MinLengthValidator(limit_value=2, message='Минимальная длина 2 символа'), CustomLenValidator(3000)))
    completion_date = forms.CharField(
        validators=(CustomDateValidator(),)
    )

    class Meta:
        model = Task
        fields = {'title', 'description', 'status',
                  'task_types', 'completion_date'}
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'task_types': 'Тип задачи',
            'completion_date': 'Выполнить до'
        }
