from django import forms

class login_form(forms.Form):
    dni = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu DNI', 'data-lpignore': 'true'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Introduce tu contraseña', 'data-lpignore': 'true'}))

class register_form(forms.Form):
    dni = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu DNI', 'autocomplete': 'off'}))
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ingresa tu nombre', 'autocomplete': 'off'}))
    surname = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingresa tus apellidos', 'autocomplete': 'off'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Introduce tu contraseña', 'autocomplete': 'off'}))