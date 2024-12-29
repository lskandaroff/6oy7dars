from django import forms
from .models import Flower, Type

class FlowerForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput())
    color = forms.CharField(max_length=100, widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())
    price = forms.IntegerField(widget=forms.NumberInput())
    photo = forms.ImageField(widget=forms.FileInput())
    type = forms.ModelChoiceField(queryset=Type.objects.all(), widget=forms.Select())

    def create(self):
        flower = Flower.objects.create(**self.cleaned_data)
        return flower

    def update(self, flower):
        flower.name = self.cleaned_data.get('name')
        flower.color = self.cleaned_data.get('color')
        flower.description = self.cleaned_data.get('description')
        flower.price = self.cleaned_data.get('price')
        flower.photo = self.cleaned_data.get('photo') if self.cleaned_data.get('photo') else flower.photo
        flower.save()

class TypeForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput())


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())







