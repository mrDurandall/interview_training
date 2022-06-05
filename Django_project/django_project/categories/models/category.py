from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models


class Category(models.Model):\

    title = models.CharField(max_length=256, verbose_name='Название категории')
    site = models.ForeignKey(Site, default=1, on_delete=models.SET(1))
    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

