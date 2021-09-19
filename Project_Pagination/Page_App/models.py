from django.db import models


class People(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=70)
    
    def __str__(self):
        return  self.name
    
    

