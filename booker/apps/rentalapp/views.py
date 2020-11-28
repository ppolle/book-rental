from booker.apps.libraryapp.models import Book
from booker.apps.rentalapp.cart import Cart
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	'''
	Render the index page
	'''
	books =  Book.objects.all()
	return render(request, 'rentalapp/index.html', {"books":books})

def book_details(request, book_id):
	'''
	view book details
	'''
	book = Book.objects.get(id=book_id)
	return render(request, 'rentalapp/book_details.html', {"book":book})

def rent_book(request, book_id):
	'''
	Add book details to rent data
	'''
	cart = Cart()
	pass