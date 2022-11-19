from django.db import models

# Create your models here.

class Product (models.Model) : #inherit model class

    name=models.CharField(max_length=255)# max lenght of name of product and type is char
    price = models.FloatField()
    stock =models.IntegerField()
    image_url =models.CharField(max_length=2083) #maxlenght of url 2083 is standard size of url
    '''
Summary. Microsoft Internet Explorer has a maximum uniform resource locator (URL) length of 2,083 characters. 
Internet Explorer also has a maximum path length of 2,048 characters. 
This limit applies to both POST request and GET request URLs
    '''

class Offer (models.Model) :
    code =models.CharField(max_length=20)
    descriptions=models.CharField(max_length=255)
    discount=models.FloatField()
