from django.db import models


class Status(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Статус"
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