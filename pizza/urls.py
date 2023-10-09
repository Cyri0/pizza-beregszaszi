from django.contrib import admin
from django.urls import path
from .views import hello

from pizzapi.views import api_map, get_toppings, get_pizzas, get_spec_pizza, get_spec_topping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', api_map),
    path('toppings/', get_toppings),
    path('pizzas/', get_pizzas),
    path('pizza/<int:pk>', get_spec_pizza),
    path('topping/<int:pk>', get_spec_topping),
]