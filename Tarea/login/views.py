from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import login_form, register_form
from django.contrib import messages
from .models import data_user
from urllib.request import urlopen
import json

# Create your views here.

def showHome(request):
    return render(request, "html/home.html")
    

def showForm(request):
    return render(request, "html/login.html", {
    'form': login_form
    })  

    '''
    if(request.method == 'GET'):
        return render(request, "html/login.html", {
        'form': login_form
        })
    else:
        
        dni = request.POST['dni']
        contraseña = request.POST['password']
        found_user = data_user.objects.get(dni=dni)

        if (contraseña == found_user.contraseña):
            return redirect("showHome")
        
        return render(request, "html/login.html", {
        'form': login_form
        })
    '''

def showRegister(request):
    if(request.method == 'GET'):
        return render(request, "html/register.html", {
            'form': register_form
        })
    else:
        dni = request.POST['dni']
        nombre = request.POST['name']
        apellidos = request.POST['surname']
        contraseña = request.POST['password']

        url = "https://dniruc.apisperu.com/api/v1/dni/" + dni + "?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImdhYnJpZWxzb3RvY2NveWFAZ21haWwuY29tIn0.BRxBA3nIZYvMzKNpljaAdICLSUa7UoGpgp7_I3qCQec"


        response = urlopen(url)
        data = json.loads(response.read())
        nombres = data.get("nombres", "")
        Api_apellidos = data.get("apellidoPaterno","") + data.get("apellidoMaterno","")

        if(isValid(nombre, nombres) and isValid(apellidos, Api_apellidos)):
            messages.success(request, "True")
            data_user.objects.create(dni=dni, nombre=nombre, apellidos=apellidos, contraseña=contraseña)
            return redirect(to="showForm")
           
        else:
            messages.error(request, "False")
            return redirect(to="showRegister")

def isValid(req, api):

    if((req.upper()).replace(" ", "").encode('utf-8') == (api.upper()).replace(" ", "").encode('utf-8') ):
        return True
    else:
        return False