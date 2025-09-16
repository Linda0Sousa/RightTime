from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    return render(request, "staff/index.html");

def create_staff(request):
    #verifies if form was send
    if request.method == "POST":
        form = StaffForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Staff criado")
        
    form = StaffForm()
        
    return render(request, "staff/new_staff.html", {"form" : form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login()
            request.session["user_id"] = user.id
            return HttpResponse(f"Login feito para: {user.email}")
        else:
            return HttpResponse("Login inválido")

    form = LoginForm()
    return render(request, "staff/login.html", {"form": form})

def create_location(request):
    #gets the user creating the location
    user = request.session["user_id"]
    
    if request.method == "POST":
        form = LocationForm(request.Post, user)
        if form.is_valid():
            user = form.login()
            return HttpResponse("feito")
        else:
            return HttpResponse("nao feito")
        
    form = LocationForm()
    return render(request, "staff/location_form.html", {"form": form})