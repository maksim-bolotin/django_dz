from django.db import models

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='URL')
    content = models.TextField(verbose_name='Содержание', **NULLABLE)
    preview = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата записи', **NULLABLE)
    publication_sign = models.BooleanField(default=True, verbose_name='Публикация')
    number_of_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f"{self.title} {self.slug} {self.content}"


class Meta:
    verbose_name = 'Пост'
    verbose_name_plural = 'Посты'
