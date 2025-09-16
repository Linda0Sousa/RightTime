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
            return HttpResponse(f"Login feito para: {user.email}")
        else:
            return HttpResponse("Login inválido")

    form = LoginForm()
    return render(request, "staff/login.html", {"form": form})