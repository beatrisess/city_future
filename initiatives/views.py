from django.shortcuts import render

# Create your views here.
from initiatives.models import Initiative
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World!')
