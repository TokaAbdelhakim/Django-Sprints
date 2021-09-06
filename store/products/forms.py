from django import forms
from .models import Product, Category

choices = [('Laptops','Laptops'), ('Accessories','Accessories'), ('Electronics','Electronics')]
''''choices = Category.objects.all().values_list('name','name')

choice_list = []
for item in choices:
    choice_list.append(item) '''


class PostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price','category')
        widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.TextInput(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),			
			'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'})		
		}
class EditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price','category')
        widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.TextInput(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),			
			'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'})			
		}

'''
 class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price')

        widgets = { 
           'name' : forms.TextInput(attrs={'class': 'form-check-label'}),
            'description' : forms.TextInput(attrs={'class': 'form-check-label'}),
            'price': forms.TextInput(attrs={'class': 'form-check-label'}), 
        }
'''