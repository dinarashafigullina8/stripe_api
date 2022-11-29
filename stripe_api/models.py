from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=255,verbose_name='Цена')
    price_id = models.CharField(max_length=255, default='-')


    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ('name',)
