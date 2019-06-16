from django.forms import ModelForm
from .models import Product,ProductImage

# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'sale_price']

class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['title', 'image', 'featured_image']
