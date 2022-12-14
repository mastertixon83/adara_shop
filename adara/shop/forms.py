from django import forms
from .models import Product


class AdminProductForm(forms.ModelForm):
    """Класс формы товара для админки"""

    class Meta:
        model = Product
        fields = ('name', 'gender', 'category', 'size_cheme', 'size', 'price', 'discount', 'description', 'slug')
        # TODO: Добавить инициализацию формы
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.SelectMultiple(attrs={'class': 'form-control chosen'})
        }

    class Media:
        js = ('https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
              'js/admin/script.js',
              )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].widget.choices ={}
