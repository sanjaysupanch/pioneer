from django.shortcuts import render
from django.http import *
from .models import *

def index(request):
    obj = student.objects.all()
    return render(request, 'index.html', {'obj': obj})
