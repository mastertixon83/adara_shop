import uuid

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

import logging

logger = logging.getLogger('main')
FEMALE = 'F'
MALE = 'M'

GENDERS = [
    (FEMALE, 'Женское'),
    (MALE, 'Мужское')
]


class Category(MPTTModel):
    """Класс модели категорий товаров"""
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDERS, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ['name']


class SizeCheme(models.Model):
    """Класс модели схемы размеров"""
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDERS, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Схема размеров'
        verbose_name_plural = 'Схемы размеров'


class Size(models.Model):
    """Класс модели размеров"""
    size_cheme = models.ForeignKey(SizeCheme, on_delete=models.CASCADE, related_name='sizes')
    rus_size = models.CharField(max_length=10)
    int_size = models.CharField(max_length=10)
    bust = models.PositiveSmallIntegerField(verbose_name='Обхват груди', default=0)
    under_bust = models.PositiveSmallIntegerField(verbose_name='Обхват под грудью', default=0)
    waist = models.PositiveSmallIntegerField(verbose_name='Обхват талии', default=0)
    hips = models.PositiveSmallIntegerField(verbose_name='Обхват бедер', default=0)
    growth = models.PositiveSmallIntegerField(verbose_name='Рост', default=0)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.rus_size} - {self.int_size}'

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Product(models.Model):
    """Класс модели продуктов"""
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='products_category'
    )
    gender = models.CharField(max_length=1, choices=GENDERS, blank=True)
    size_cheme = models.ForeignKey(
        SizeCheme,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='size_themes'
    )
    size = models.ManyToManyField(Size, related_name='product_sizes')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    #TODO: назначить изображение по умолчанию
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    articul = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    """Класс модели изображений для товара"""
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images_product')
    image = models.ImageField(upload_to='products/%Y/%m/%d')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['pk']


@receiver(post_save, sender=ProductImage)
def get_image_for_main_product_image(sender, instance, **kwargs):
    """
    Сигнал post save модели ProductImage
    Добавляет главное изображение для товара
    """
    product = instance.product
    images = product.images_product.all()
    product.image = images[0].image
    product.save()

    logger.debug(images)


@receiver(post_delete, sender=ProductImage)
def clear_main_image_from_product(sender, instance, **kwargs):
    """
    Сигнал post delete модели ProductImage
    Удаляет главное изображение для товара
    """
    product = instance.product
    images = product.images_product.all()
    if images.count() == 0:
        product.image = ''
    else:
        product.image = images[0].image
    product.save()
