from django import forms
from .models import Textile
from .models import Cart


# from django.utils.safestring import mark_safe


# class PictureWidget(forms.widgets.Widget):
#     def render(self, name, value, attrs=None):
#         html = Template("""<img src="$link"/>""")
#         return mark_safe(html.substitute(link=value))
#
#
class TextileForm(forms.ModelForm):
    #     image = ImageField(widget=PictureWidget)
    class Meta:
        model = Textile
        fields = [
            'title',
            'description',
            'price',
            'offer',
            'image',
        ]

#
# class CartForm(forms.ModelForm):
#     class Meta:
#         model = Cart
#         fields = [
#             'quantity',
#             'size'
#         ]
