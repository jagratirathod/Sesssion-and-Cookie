from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hii(request):
    return HttpResponse("smile")