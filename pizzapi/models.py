from django.db import models

# Create your models here.

class Topping(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name
    
    def serialize(self):
        topp_li = []
        
        for topping in self.toppings.all():
            topp_li.append(topping.serialize())

        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "toppings": topp_li
        }
