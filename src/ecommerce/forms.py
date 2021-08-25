from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User= get_user_model()

class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Your Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "Your Email Address"}))
    phone = forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Your Phone"})
    dob = forms.DateField(widget=forms.SelectDateWidget(
        attrs={"class": "form-control", "placeholder": "Your Email Address"}))


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail")
        return email

class LoginForm(forms.Form):
    username= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username= forms.CharField()
    email=forms.CharField(widget=forms.EmailInput())
    password= forms.CharField(widget=forms.PasswordInput())
    confirm_password= forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username= self.cleaned_data['username']
        qs= User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username taken")
        return username

    def clean_email(self):
        email= self.cleaned_data['email']
        qs= User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = data['password']
        confirm_password = data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return data
    
    
