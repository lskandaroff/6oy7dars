from django import forms
from .models import Flower, Type

class FlowerForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput())
    color = forms.CharField(max_length=100, widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())
    price = forms.IntegerField(widget=forms.NumberInput())
    photo = forms.ImageField(widget=forms.FileInput())
    type = forms.ModelChoiceField(queryset=Type.objects.all(), widget=forms.Select())

class TypeForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput())





