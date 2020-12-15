from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    index  view
    """
    return  HttpResponse("Hello, world, You are at the polls index.")   


