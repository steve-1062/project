from django.shortcuts import render
from django.http import HttpResponse
from .models import*
import logging

# Create your views here.

def home(request):
    return render(request, "dashboard/home.html")

def products(request):
    products = product.objects.all()
    img = "static/images/"

    return render(request, 'dashboard/products.html', {'products':products, 'img':img})

def customer(request):
    return render(request, "dashboard/customer.html")

def cart(request):
   
    try:
        items = request.COOKIES.get('cart')
        items = set(items[1:-1].replace("\"",'').split(","))
        
        products = []
        print(request.COOKIES.get('cart'))
        for i in items:
            products.append(product.objects.filter(product_id = i ).get())
        print("\n\n\n\n\n\n",products)
        response = render(request, 'dashboard/cart.html', { 'product' : products}) 
        return(response)
    except Exception as e:
        print(e)
        return(render(request, 'dashboard/cart.html', { 'msg' : "Cart is empty"}))