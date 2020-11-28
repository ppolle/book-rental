from django.test import TestCase
from datetime import date, timedelta
from booker.apps.libraryapp.models import Book
from django.urls import reverse

class ViewTests(TestCase):
	def setUp(self):
		self.session = self.client.session
		self.book_1 = Book.objects.create(title='A man of the people',description='A novel by chinua achebe about a man of the people.')
		self.book_2 = Book.objects.create(title='Drunk', description='A book by Steve Biko about a man struggling with his drinking demons')
		self.book_3 = Book.objects.create(title='Green Belt', description='A book about conservation of forests')

	def add_book_to_sessions(self):
		
		url_1 = reverse('book_details',kwargs={'book_id':self.book_1.id})
		data_1 = {'start_date':date.today(),'end_date':date.today()+timdelta(days=5)}
		response_1 = self.client.post(url_1, data_1, follow=True)
		
		url_2 = reverse('book_details',kwargs={'book_id':self.book_2.id})
		data_2 = {'start_date':date.today()+timedelta(days=2),'end_date':date.today()+timdelta(days=5)}
		response_2 = self.client.post(url_2, data_2, follow=True)
		
		self.assertEqual(len(self.session['cart']), 2)
		self.assertEqual(response_1.status_code, 200)
		self.assertEqual(response_2.status_code, 200)

	def delete_book_from_sessions(self):
		url = reverse('delete_cart_item', kwargs={'book_id':self.book_2.id})
		response = self.client.get(url)

		self.assertEqual(len(self.session['cart']), 1)
		self.assertEqual(response.status_code, 200)

	def clear_all_session(self):
		url = reverse('clear_cart')
		response = self.client.get(url)

		self.assertEqual(len(self.session['cart']), 0)
		self.assertEqual(response.status_code, 200)
