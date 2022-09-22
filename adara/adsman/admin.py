from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    """Класс регистрации баннеров модели в админке"""
    save_on_top = True
    save_as = True
    save_as_continue = True

    list_display = ('pk', 'banner_position', 'draft', 'get_image')
    readonly_fields = ('get_image',)
    list_display_links = ['pk', 'banner_position']
    list_editable = ['draft']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="60" height="60"')

    get_image.short_description = 'Изображение'


admin.site.site_title = "Adara Shop - Ads Manager"
admin.site.site_header = "Adara Shop - Ads Manager"