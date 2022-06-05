from django.db import models


class HitCount(models.Model):
    path = models.CharField(max_length=512, verbose_name='Путь')
    hits = models.IntegerField(default=1, verbose_name='Количество обращений')
    user = models.ForeignKey('auth.User',
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Счетчик посещения'
        verbose_name_plural = 'Счетчики'

    def __str__(self):
        return f'Обращения пользователя {self.user} по адресу {self.path} - ({self.hits})'
