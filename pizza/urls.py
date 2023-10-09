from django.contrib import admin
from django.urls import path
from .views import hello

from pizzapi.views import api_map, get_toppings, get_pizzas, get_spec_pizza

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', api_map),
    path('toppings/', get_toppings),
    path('pizzas/', get_pizzas),
    path('pizza/<int:pk>', get_spec_pizza)
]