from django.db import models


class Good(models.Model):

    class Units(models.TextChoices):

        KILOGRAMS = 'kg', 'Килограммы'
        METERS = 'm', 'Метры'
        PIECES = 'pi', 'Штуки'
        PACKAGES = 'pa', 'Упаковки'

    title = models.CharField(max_length=256, verbose_name='Наименование')
    supply_date = models.DateField(verbose_name='Дата поступления', auto_now_add=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    unit = models.CharField(max_length=2,
                            choices=Units.choices,
                            default=Units.PIECES,
                            verbose_name='Единицы измерения')
    supplier = models.ForeignKey('common.Supplier',
                                 related_name='good',
                                 verbose_name='Поставщик',
                                 on_delete=models.CASCADE,
                                 )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
