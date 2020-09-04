from django import forms
from django.contrib.auth.models import User
from .models import Producto
from django.forms import ModelForm

class LoginForms(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label="User Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password_1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'},
                                                                              render_value=False))
    password_2 = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(attrs={'class': 'form-control'},
                                                                                        render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        username = username.lower()
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Nombre de usuario ya existe")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("Email ya registrado")

    def clean_password_2(self):
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if password_1 == password_2:
            pass
        else:
            raise forms.ValidationError("Passwords no coinciden")

