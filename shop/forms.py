from django import forms
from .models import Comment, Purchase
# from .models import ProductImage


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body')

class CartCreationForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('count',)

# class ProductImageForm(forms.ModelForm):
#     class Meta:
#         model = ProductImageForm
#         fields = ('title', 'description', 'care', 'image')
