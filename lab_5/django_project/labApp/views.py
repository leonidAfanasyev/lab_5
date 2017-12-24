from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from .models import  *

def home(request):
    par = {
        'header': 'Home'
    }
    return render(request, 'home.html', context=par)


class CustomerView(ListView):
    model = Customer
    template_name = 'customer_list.html'


class ProdactsView(ListView):
    model = Prodact
    template_name = 'prodacts.html'
    context_object_name = 'prodacts_list'


class OrderView(ListView):
    model = Order
    template_name = 'order_list.html'
