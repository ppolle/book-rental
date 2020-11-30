from django.conf import settings
from booker.apps.rentalapp.models import Book
class Cart:
	def __init__(self, request):
		self.session = request.session

		if self.session.has_key(settings.CART_SESSION_ID):
			self.cart = self.session[settings.CART_SESSION_ID]
		else:
			self.cart = self.session[settings.CART_SESSION_ID] = {}

	def add(self, book, start_date, stop_date):
		'''
		Add a book item to the cart
		'''
		book_id = book.id
		rent = book.calculate_cost(start_date,stop_date)

		self.cart[book_id] = {"rent":float(rent),"start_date":str(start_date),"stop_date":str(stop_date)}

		self.save()

	def save(self):
		'''
		save book items to the session
		'''
		self.session[settings.CART_SESSION_ID] = self.cart
		self.session.modified = True

	def remove(self, book):
		'''
		Remove a book from the session
		'''
		book_id = str(book.id)
		if book_id in self.cart:
			del self.cart[book_id]

		self.save()

	def clear(self):
		'''
		Clear the entire session
		'''
		del self.session[settings.CART_SESSION_ID]

	def total_rental_cost(self):
		'''
		Get total cost of renting all availble books
		'''
		return sum(float(item['rent']) for item in self.cart.values())

	def __iter__(self):
		book_ids = self.cart.keys()
		books = Book.objects.filter(id__in=book_ids)

		for book in books:
			self.cart[str(book.id)]['book'] = book

		for item in self.cart.values():
			yield item

	def __len__(self):
		return len(self.cart)

