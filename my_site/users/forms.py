
from django import forms

from .models import Users

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    username=forms.CharField(widget=forms.TextInput, label='Логин')
    email=forms.EmailField(widget=forms.EmailInput, label='Электронная почта')
    age=forms.CharField(widget=forms.TextInput, max_length=3, label='Возраст')
    class Meta:
        model = Users
        fields = ['username', 'password', 'age', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")


class Avtorizations(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    username = forms.CharField(widget=forms.TextInput, label='Логин')
    class Meta:
        model = Users
        fields = ['username', 'password']