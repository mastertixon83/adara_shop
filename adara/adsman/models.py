from django.db import models


class Banner(models.Model):
    """Класс модели баннеров"""
    MENUBANNER = 'MB'
    GENDERBANNER = 'GB'
    SLIDER = 'SL'
    TOPBANNER1 = 'TB1'
    TOPBANNER2 = 'TB2'
    TOPBANNER3 = 'TB3'
    TOPBANNER4 = 'TB4'
    DISCOUNTBANNER = 'DB'
    DISCOUNTICON = 'DI'
    TRENDINGBANNER = 'TB'
    BRANDS = 'BR'
    INSTAGRAM = 'IG'
    BANNER_POSITIONS = [
        (GENDERBANNER, 'Gender Banner 300x345'),
        (MENUBANNER, 'Menu Banner 250x170'),
        (SLIDER, 'Top Slider 960x900'),
        (TOPBANNER1, 'Banner1 870x800'),
        (TOPBANNER2, 'Banner2 425x390'),
        (TOPBANNER3, 'Banner3 425x390'),
        (TOPBANNER4, 'Banner4 870x390'),
        (DISCOUNTBANNER, 'Discount banner 1920x1080'),
        (DISCOUNTICON, 'Discount Icon 94x94'),
        (TRENDINGBANNER, 'Trending Banner '),
        (BRANDS, 'Brands Banner 180x60'),
        (INSTAGRAM, 'Instagram Banner 385x350'),
    ]

    banner_position = models.CharField(
        max_length=3,
        choices=BANNER_POSITIONS,
    )
    image = models.ImageField(upload_to='banners/%Y/%m/%d')
    url = models.URLField(blank=True)
    text1 = models.CharField(max_length=100, blank=True)
    text2 = models.CharField(max_length=100, blank=True)
    text3 = models.CharField(max_length=100, blank=True)
    draft = models.BooleanField(default=False, verbose_name='Черновик')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.banner_position

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['pk']