from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin

from .forms import AdminProductForm

from .models import Category, Product, ProductImage, SizeCheme, Size
import logging

logger = logging.getLogger('main')


# admin.site.register(
#     Category,
#     DraggableMPTTAdmin,
#     list_display=(
#         'tree_actions',
#         'indented_title',
#         # ...more fields if you feel like it...
#     ),
#     list_display_links=(
#         'indented_title',
#     ),
# )


@admin.register(SizeCheme)
class SizeChemeAdmin(admin.ModelAdmin):
    """Класс регистрации модели размерных сеток в админке"""
    save_on_top = True
    save_as = True
    save_as_continue = True

    prepopulated_fields = {"slug": ("name",)}

    list_display = ['pk', 'name', 'gender']
    list_display_links = ['pk', 'name']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    """Класс регистрации модели размеров в админке"""
    save_on_top = True
    save_as = True
    save_as_continue = True

    prepopulated_fields = prepopulated_fields = {"slug": ("rus_size", "int_size")}

    list_display = ['pk', 'rus_size', 'int_size', 'size_cheme']
    list_display_links = ['pk', 'rus_size', 'int_size']


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    """Класс регистрации модели катеорий в админке"""
    save_on_top = True
    save_as = True
    save_as_continue = True

    prepopulated_fields = {"slug": ("name")}

    list_display = ['gender', 'tree_actions', 'indented_title', 'pk', 'slug']
    list_display_links = ['pk', 'indented_title']


class ImagesInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    list_display = ['pk', 'name', 'image', 'get_image']
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="60" height="60"')

    get_image.short_description = 'Изображение'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс регистрации модели товаров в админке"""
    save_on_top = True
    save_as = True
    save_as_continue = True
    form = AdminProductForm
    prepopulated_fields = {"slug": ("name",)}
    # class Media:
    #     js = ('https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
    #         'js/admin/script.js',
    #     )
    #
    # prepopulated_fields = {"slug": ("name",)}
    #
    # list_display = ['pk', 'name', 'gender', 'category', 'draft', 'featured', 'trending', 'get_image']
    # list_editable = ['draft', 'featured', 'trending']
    # list_display_links = ['pk', 'name']
    # exclude = ['image']
    # readonly_fields = ('get_image',)
    # inlines = [ImagesInline]
    #
    # def get_image(self, obj):
    #     if obj.image:
    #         return mark_safe(f'<img src={obj.image.url} width="60" height="60"')
    #
    # get_image.short_description = 'Изображение'


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """Класс регистрации модели изображений товара в админке"""
    model = ProductImage
    save_on_top = True
    save_as = True
    save_as_continue = True

    list_display = ['pk', 'name', 'product', 'get_image']
    list_display_links = ['pk', 'name']

    readonly_fields = ['get_image', ]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="60" height="60"')

    get_image.short_description = 'Изображение'


admin.site.site_title = "Adara Shop - Shop"
admin.site.site_header = "Adara Shop - Shop"
