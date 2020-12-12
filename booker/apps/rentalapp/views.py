from django.db import transaction
from booker.apps.rentalapp.cart import Cart
from django.shortcuts import render, redirect
from booker.apps.libraryapp.models import Book
from booker.apps.rentalapp.models import Rent, RentItem
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
		data = {"book_id":book_id}
		form = RentBookForm(initial=data)

	return render(request, 'rentalapp/book_details.html', {"book":book, "form":form})

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

def checkout(request):
	'''
	Record all cart items as having been booked
	'''
	cart = Cart(request)
	if len(cart) > 0:
		with transaction.atomic():
			rent = Rent.objects.create(total=cart.total_rental_cost())

			for item in cart:
				print(type(item['start_date']))
				RentItem.objects.create(
    rent=rent, book=item['book'], start_date=item['start_date'], stop_date=item['stop_date'])
		cart.clear()

	return redirect('index')

def view_cart(request):
	'''
	View cart items
	'''
	cart = Cart(request)
	return render(request, 'rentalapp/cart.html', {'cart':cart})

def view_test_coverage(request):
	return render(request, 'cover/index.html')