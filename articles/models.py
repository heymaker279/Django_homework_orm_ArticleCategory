from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=30, verbose_name='Разделы')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scope = models.ManyToManyField(Section, verbose_name='Статьи', through='ArticleSection')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'



