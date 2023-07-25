from django.shortcuts import render
from .forms import login_form, register_form

# Create your views here.

def showForm(request):
    return render(request, "html/login.html", {
        'form': login_form
    })

def showRegister(request):
    return render(request, "html/register.html", {
        'form': register_form
    })