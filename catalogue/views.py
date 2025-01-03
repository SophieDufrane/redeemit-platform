from django.shortcuts import render
from django.http import HttpResponse

def hello_catalogue(request):
    return HttpResponse("Hello, Redemption Catalogue!")

# Create your views here.
