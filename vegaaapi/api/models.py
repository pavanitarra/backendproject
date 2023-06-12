from django.db import models

# Create your models here.


class Location(models.Model):
    name= models.CharField(unique=True, max_length=100)
    #type= models.CharField(max_length=50,choices=(('vo','vo'),('bg','bg')))

    def __str__(self):
        return self.name
        


class Item(models.Model):
    name = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    type= models.CharField(max_length=50,choices=(('vo','vo'),('bg','bg')))
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name