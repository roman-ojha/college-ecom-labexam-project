from django.shortcuts import render
from app import models

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
    if book != None:
        response.set_cookie('cart', [book.slug])
    return response
