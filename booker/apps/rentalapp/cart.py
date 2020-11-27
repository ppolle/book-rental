from django.conf import settings


class Cart:
	def __init__(self, request):
		self.session = request.session

		if self.session.has_key(settings.CART_SESSION_ID):
			self.cart = self.session[settings.CART_SESSION_ID]
		else:
			self.cart = self.session[settings.CART_SESSION_ID] = {}

	def add(self, book):
		'''
		Add a book item to the cart
		'''
		book_id = book.id

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