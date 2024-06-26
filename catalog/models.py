from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    category_description = models.TextField(verbose_name='Описание', **NULLABLE)
    category_image = models.ImageField(upload_to='image/', verbose_name='Изображение категории', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}, {self.category_description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название')
    product_description = models.CharField(max_length=100, verbose_name='Описание', **NULLABLE)
    product_image = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    product_price = models.IntegerField(verbose_name='Цена', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата записи', **NULLABLE)
    updated_at = models.DateField(auto_now_add=True, verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return (f'{self.product_name}'
                f'{self.product_price}'
                f'{self.product_category}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    version_number = models.IntegerField(default=0, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='описание', **NULLABLE)
    version_sign = models.BooleanField(default=True, verbose_name='версия')
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Название')

    def __str__(self):
        return f'{self.version_number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
