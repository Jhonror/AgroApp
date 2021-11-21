from django.db import models

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField('Description', max_length = 15, unique=True)
    price = models.CharField('Price', max_length = 256)  
    stock = models.FloatField('Stock') 
    unit_m =models.CharField('Unit_m', max_length = 256)  
    
    
    def __str__(self):
        return self.name
    
    
