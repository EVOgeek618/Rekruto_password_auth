from django import forms

class User(forms.Form):

    login = forms.CharField(max_length=30, min_length=4)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6)