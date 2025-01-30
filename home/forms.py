from django import forms
from django.contrib.auth.models import User

class CustomSignupForm(forms.ModelForm):
    """
    Custom signup form replacing default username with first and last name.
    """
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"})
    )
    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
