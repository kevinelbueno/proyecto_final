# forms.py

from django import forms
from .models import Art

class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['art_name', 'author', 'price', 'style', 'image', 'description']
        widgets = {
            'art_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),  # Cambiado de Select a TextInput porque 'author' es un campo de texto
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'style': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
