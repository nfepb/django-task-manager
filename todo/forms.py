from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """
    Meta class gives our form some information about itself,
    such as which fields to render, or how to display errors.
    The fields: name and done, have already been defined in models.py
    """
    class Meta:
        model = Item
        fields = ['name', 'done']
