from django import forms
from django.forms import ModelForm

from car.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'price', 'brand', 'description', 'photo']