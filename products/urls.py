from django.urls import path
from . import views
#/product =root ="" endpoint

urlpatterns =[

    path("",views.index) ,# just pass refernces django will call at the time of request
    path("new",views.new)
]