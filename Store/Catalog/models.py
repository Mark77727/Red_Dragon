from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

""" 1. Entity Category"""


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Категория'

    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name


""" 2. Entity. Catalog """


class Catalog(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',

    )

    product_name = models.CharField(
        max_length=50,
        verbose_name='Видеокарта',
        blank=False,

    )

    GPU = models.CharField(
        max_length=50,
        verbose_name='Графический процессор',
        blank=False,

    )

    manufacturer_GPU = models.CharField(
        max_length=50,
        verbose_name='Производитель ГП',
        blank=False,

    )

    memory_type = models.CharField(
        max_length=50,
        verbose_name='Тип памяти',
        blank=False,

    )

    power_connector = models.CharField(
        max_length=50,
        verbose_name='Разъем питания',
        blank=False,

    )

    video_connector = models.CharField(
        max_length=50,
        verbose_name='Видеоразъем',
        blank=False,

    )

    price = models.PositiveBigIntegerField(
        default=0,
        verbose_name='Цена',

    )

    brand = models.CharField(
        max_length=50,
        verbose_name='Бренд',

    )

    video_memory_capacity = models.IntegerField(
        default=0,
        verbose_name='Объем видеопамяти',

    )

    frequency_GPU = models.IntegerField(
        default=0,
        verbose_name='Частота ГП',

    )

    video_card_length = models.IntegerField(
        default=0,
        verbose_name='Длина',

    )

    discount = models.BooleanField(
        verbose_name='Акция',

    )

    new = models.BooleanField(
        verbose_name='Новинка',

    )

    class Meta:
        verbose_name = ' КАТАЛОГ'
        verbose_name_plural = ' КАТАЛОГ'

    def __str__(self):
        return self.product_name
