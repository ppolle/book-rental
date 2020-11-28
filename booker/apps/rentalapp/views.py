from booker.apps.rentalapp.cart import Cart
from django.shortcuts import render, redirect
from booker.apps.libraryapp.models import Book
from booker.apps.rentalapp.forms import RentBookForm

# Create your views here.
def index(request):
	'''
	Render the index page
	'''
	cart  = Cart(request)
	books =  Book.objects.all()
	return render(request, 'rentalapp/index.html', {"books":books,"cart":cart})

def book_details(request, book_id):
	'''
	view book details
	'''
	book = Book.objects.get(id=book_id)
	if request.method == 'POST':
		form = RentBookForm(request.POST)
		if form.is_valid():
			start_date = form.cleaned_data['start_date']
			stop_date = form.cleaned_data['end_date']

			cart = Cart(request)
			cart.add(book,start_date, stop_date)
			return redirect('index')
	else:
		form = RentBookForm()

	return render(request, 'rentalapp/book_details.html', {"book":book, "form":form})

def rent_book(request, book_id):
	'''
	Add book details to rent data
	'''
	cart = Cart()
	pass

def delete_cart_item(request, book_id):
	'''
	Delete cart item
	'''
	cart = Cart(request)
	book = Book.objects.get(id=book_id)
	cart.remove(book)

	return redirect('index')

def clear_cart_items(request):
	'''
	Clear all the items in the cart list
	'''
	cart = Cart(request)
	cart.clear()
	return redirect('index')
