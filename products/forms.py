from django import forms
from .models import Product, Category


class ProductForm(form.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwars)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.field['category'].choices = friendly_name
        for field_name, field in self.field.item():
            field.widget.attrs['class'] = 'border-black rounded-0'