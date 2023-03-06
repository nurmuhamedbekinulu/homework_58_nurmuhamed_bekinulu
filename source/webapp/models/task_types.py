from django.db import models


class Task_type(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Тип задачи"
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время и дата создания"
        )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Время и дата обновления"
        )

    def __str__(self):
        return self.name