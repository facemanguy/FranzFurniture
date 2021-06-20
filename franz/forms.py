from django import forms
from .models import FurnitureType, Furniture, FurnitureDetails

class FurnitureForm(forms.ModelForm):
    class Meta:
        model=Furniture
        fields='__all__'

