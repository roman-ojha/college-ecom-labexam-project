from django.shortcuts import render
from app import models
import requests

# Create your views here.


def index(request):
    books = models.Book.objects.all()
    return render(request, 'index.html', context={'books': books})


def book(request, slug):
    book = models.Book.objects.filter(slug=slug).first()
    return render(request, 'book.html', context={'book': book})


def add_to_cart(request, slug):
    book = models.Book.objects.filter(slug=slug).first()
    response = render(request, 'book.html', context={'book': book})
    if book == None:
        return response
    response.set_cookie('cart', [book.slug])
    return response


def get_cart(request):
    carts = request.COOKIES.get('cart')
    if carts is None:
        return render(request, 'cart.html')

    # Remove the outer single quotes and use split to get the elements
    elements = carts[1:-1].split(', ')

    # Convert the elements to a Python list
    cart_items = [element.strip("'") for element in elements]

    carts = models.Book.objects.filter(slug=cart_items[0])
    total = 0
    for cart in carts:
        total += cart.price
    return render(request, 'cart.html', context={'carts': carts, 'total': total})


def checkout(request):
    requestHeader = {"Authorization": "Key "}
    requestParameters = {
        "return_url": "http://127.0.0.1:8000" + "/api/payment/success",
        "website_url": "http://127.0.0.1:8000",
        "amount": 3000,
        "purchase_order_id": f"HAMROROJGAR-fds-rfda-fdsa",
        "purchase_order_name": f"job application payment",
    }
    # request to khalti to initiate the payment
    response = requests.post(
        "https://a.khalti.com/api/v2" + "/epayment/initiate/", headers=requestHeader, data=requestParameters)
    if response.status_code == 200:
        print(response)

    return render(request, 'cart.html')
