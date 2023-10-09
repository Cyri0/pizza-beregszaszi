from django.http import JsonResponse
from .models import Pizza, Topping

# Create your views here.

def api_map(request):

    enpoints = {
        "/":"This page",
        "/pizzas":"Return all pizza",
        "/pizza/<id>":"Return one spec. pizza",
        "/toppings":"Return all toppings",
        "/topping/<id>":"Return one topping by ID"
    }

    return JsonResponse(enpoints)

def get_toppings(request):
    toppings = Topping.objects.all()
    li = []

    for topping in toppings:
        li.append(topping.serialize())

    return JsonResponse({"data": li})

def get_pizzas(request):
    pizzas = Pizza.objects.all()
    li = []

    for pizza in pizzas:
        li.append(pizza.serialize())

    return JsonResponse({"data": li})

def get_spec_pizza(request, pk):
    pizza = Pizza.objects.get(id = pk)
    return JsonResponse(pizza.serialize())
