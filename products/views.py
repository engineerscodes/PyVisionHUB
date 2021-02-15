from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#.products ->index must be rendered

def index(request):
    return HttpResponse("<h1>NAVEEN </h1>")