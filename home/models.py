from django.db import models

# Create your models here.
class PriceList(models.Model):
    '''Модель прайс листа'''
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    file = models.FileField(upload_to='', verbose_name='Файл')
    counter = models.PositiveIntegerField(default=0, verbose_name='Кол-во загрузок')
    is_active = models.BooleanField(default=True, verbose_name='Модерация')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Прайс лист'
        verbose_name_plural = 'Прайс листы'
        ordering = ['-created']