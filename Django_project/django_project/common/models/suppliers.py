from django.db import models


class Supplier(models.Model):

    title = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.title
