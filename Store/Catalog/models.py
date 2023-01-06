from django.db import models

""" 1. Entity Category"""


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Категория'

    )

    slug = models.SlugField(
        max_length=255,
        verbose_name='URL'

    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name


""" 2. Entity. Brand """


class Brand(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Бренд',
        blank=False,

    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'

    def __str__(self):
        return self.name


""" 3. Entity. GPU """


class GPU(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Графический процессор',
        blank=False,

    )

    class Meta:
        verbose_name = 'Графический процессор'
        verbose_name_plural = 'Графический процессор'

    def __str__(self):
        return self.name


""" 4. Entity. GPU manufacturer """


class ManufacturerGPU(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Производитель ГП',
        blank=False,

    )

    class Meta:
        verbose_name = 'Производитель ГП'
        verbose_name_plural = 'Производитель ГП'

    def __str__(self):
        return self.name


""" 5. Entity. Memory type """


class MemoryType(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Тип памяти',
        blank=False,

    )

    class Meta:
        verbose_name = 'Тип памяти'
        verbose_name_plural = 'Тип памяти'

    def __str__(self):
        return self.name


""" 6. Entity. Power connector """


class PowerConnector(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Разъем питания',
        blank=False,

    )

    class Meta:
        verbose_name = 'Разъем питания'
        verbose_name_plural = 'Разъем питания'

    def __str__(self):
        return self.name


""" 7. Entity. Video connector """


class VideoConnector(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Видеоразъем',
        blank=False,

    )

    class Meta:
        verbose_name = 'Видеоразъем'
        verbose_name_plural = 'Видеоразъем'

    def __str__(self):
        return self.name


""" 8. Entity. Summary table """


class Catalog(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'

    )

    product_name = models.CharField(
        max_length=20,
        verbose_name='Видеокарта',
        blank=False,

    )

    slug = models.SlugField(
        max_length=255,
        verbose_name='URL',
    )

    price = models.IntegerField(
        default=0,
        verbose_name='Цена',

    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Бренд',

    )

    GPU = models.ForeignKey(
        GPU,
        on_delete=models.CASCADE,
        verbose_name='Графический процессор',

    )

    manufacturer_GPU = models.ForeignKey(
        ManufacturerGPU,
        on_delete=models.CASCADE,
        verbose_name='Производитель ГП',

    )

    memory_type = models.ForeignKey(
        MemoryType,
        on_delete=models.CASCADE,
        verbose_name='Тип памяти',

    )

    video_memory_capacity = models.IntegerField(
        default=0,
        verbose_name='Объем видеопамяти',

    )

    frequency_GPU = models.IntegerField(
        default=0,
        verbose_name='Частота ГП',

    )

    power_connector = models.ForeignKey(
        PowerConnector,
        on_delete=models.CASCADE,
        verbose_name='Разъем питания',

    )

    video_connector = models.ForeignKey(
        VideoConnector,
        on_delete=models.CASCADE,
        verbose_name='Видеоразъем',

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
        return self.category
