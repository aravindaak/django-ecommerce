from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title": "Home Page"
    }
    return render(request, "home.html", context)

def form_page(request):
    form= ContactForm(request.POST or None)
    context = {
        "title": "Form Page",
        "form": form
    }
    return render(request, "forms/form.html", context)

def login_page(request):
    form=LoginForm(request.POST or None)
    context={
        "form": form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            print("Error")
    return render(request, "auth/login.html", context)


User= get_user_model()
def register_page(request):
    form=RegisterForm(request.POST or None)
    context={
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username= form.cleaned_data.get("username")
        email= form.cleaned_data.get("email")
        password= form.cleaned_data.get("password")
        new_user= User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)
