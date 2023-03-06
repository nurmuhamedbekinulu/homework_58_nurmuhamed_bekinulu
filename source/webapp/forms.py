from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from webapp.models import Task
from datetime import datetime


class TaskForm(forms.ModelForm):
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

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return title

    def clean_description(self):
        title = self.cleaned_data.get('description')
        if len(title) < 2:
            raise ValidationError('Описание должено быть длиннее 2 символов')
        return title