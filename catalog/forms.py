from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            if fild_name != "version_sign":
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенное слово в названии')
            return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    version_sign = forms.BooleanField(label='Активная версия', required=False)

    class Meta:
        model = Version
        fields = '__all__'
