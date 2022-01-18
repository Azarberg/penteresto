from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

<<<<<<< HEAD
# Create your models here.


class News(models.Model):
    title = models.CharField(verbose_name='Название', blank=True,
                             max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    teg = models.ForeignKey('Tegs', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
=======

class Blog(models.Model):
    title = models.CharField(
        max_length=160,
        verbose_name='Заголовок',
        db_index=True)
    text = models.TextField(
        blank=True,
        verbose_name='Контент')
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        verbose_name='Изображение')
    publish_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата Публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='Автор')
    is_published = models.BooleanField(
        default=True,
        verbose_name='Состаяние публикации')
    category = models.ForeignKey(
        "Category",
        on_delete=models.DO_NOTHING,
        verbose_name='Категория')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-publish_date']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(
        max_length=220,
        verbose_name='Категории')
    slug = models.SlugField(
        max_length=220,
        verbose_name='Url')
>>>>>>> 96ddef49809f5bbf9b3fa24fbe319dee62809744

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']

<<<<<<< HEAD

class Views(models.Model):
    title = models.CharField(max_length=20)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.views}'


class Likes(models.Model):
    title = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.likes}'


class Comments(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=55)
    comment = models.TextField('Комментарий', max_length=255)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-comment']


class Tegs(models.Model):
    teg = models.CharField(max_length=255)

    def __str__(self):
        return self.teg

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-teg']
=======
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
>>>>>>> 96ddef49809f5bbf9b3fa24fbe319dee62809744
