from django import forms
from django.core.exceptions import ValidationError

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

def username_validator(value):
    if ' ' in value:
        raise ValidationError('usernameda bosh joy bolishi mumkun emas')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(), validators=[username_validator])
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput())


    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')
        if password_repeat != password:
            raise ValidationError('parollar bir xil  bolishi kerak')

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())



class CommentForm(forms.Form):
    text = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 3,
        "maxlength": 1000
    }), label="Comment matni")








