from django.shortcuts import render
from django.urls import reverser_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateform()
    success_url = reverser_lazy('login')
    template_name = 'accounts/signup.html'