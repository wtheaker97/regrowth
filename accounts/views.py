# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic

from . import forms


# class SignUpView(generic.CreateView):
#     form_class = forms.SignUpForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        form = forms.SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
