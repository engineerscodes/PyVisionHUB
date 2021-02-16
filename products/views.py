from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#.products ->index must be rendered

from .models import Product

def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products' :products})

#<!--{%%} template tag used for dynamic logics like loop and if-->
#<!--Dyanmically render values use {{}}-->











def new(request):
    return HttpResponse("<h1><i> NEW PRODUCTS </i></h1>")