from django.urls import reverse
from django.conf import settings
from django.test import TestCase, RequestFactory
from datetime import date, timedelta
from booker.apps.libraryapp.models import Book, BookType
from booker.apps.rentalapp.models import Rent, RentItem
from booker.apps.rentalapp.cart import Cart
class RentalAppViewTests(TestCase):
	def setUp(self):
		self.session = self.client.session
		self.session[settings.CART_SESSION_ID] = {}
		self.session.save()

		self.novel = BookType.objects.create(name='novel', daily_rate=1.50)
		self.fiction = BookType.objects.create(name='fiction', daily_rate=3.00)
		self.regular = BookType.objects.create(name='regular', daily_rate=1.50)

		self.book_1 = Book.objects.create(title='A man of the people',description='A novel by chinua achebe about a man of the people.', genre=self.novel)
		self.book_2 = Book.objects.create(title='Drunk', description='A book by Steve Biko about a man struggling with his drinking demons', genre=self.fiction)
		self.book_3 = Book.objects.create(title='Green Belt', description='A book about conservation of forests', genre=self.regular)

	def test_add_book_to_sessions(self):
		
		url_1 = reverse('book_details',kwargs={'book_id':self.book_1.id})
		data_1 = {'start_date':date.today(),'end_date':date.today()+timedelta(days=5)}
		response_1 = self.client.post(url_1, data_1, follow=True)
		
		url_2 = reverse('book_details',kwargs={'book_id':self.book_2.id})
		data_2 = {'start_date':date.today()+timedelta(days=2),'end_date':date.today()+timedelta(days=5)}
		response_2 = self.client.post(url_2, data_2, follow=True)
		
		self.assertEqual(len(self.session[settings.CART_SESSION_ID]), 2)
		self.assertEqual(response_1.status_code, 200)
		self.assertEqual(response_2.status_code, 200)

	def test_delete_book_from_sessions(self):
		url = reverse('delete_cart_item', kwargs={'book_id':self.book_2.id})
		response = self.client.get(url)

		self.assertEqual(len(self.session[settings.CART_SESSION_ID]), 1)
		self.assertEqual(response.status_code, 200)

	def test_clear_all_session(self):
		self.assertEqual(len(self.session[settings.CART_SESSION_ID]), 1)
		url = reverse('clear_cart')
		response = self.client.get(url, follow=True)

		self.assertEqual(len(self.session[settings.CART_SESSION_ID]), 0)
		self.assertEqual(response.status_code, 200)

	def test_session_is_cleared_on_checkout(self):
		url_1 = reverse('book_details',kwargs={'book_id':self.book_1.id})
		data_1 = {'start_date':date.today(),'end_date':date.today()+timedelta(days=5)}
		response_1 = self.client.post(url_1, data_1, follow=True)
		
		url_2 = reverse('book_details',kwargs={'book_id':self.book_2.id})
		data_2 = {'start_date':date.today()+timedelta(days=2),'end_date':date.today()+timedelta(days=5)}
		response_2 = self.client.post(url_2, data_2, follow=True)

		url_3 = reverse('checkout')
		response_3 = self.client.get(url_3, follow=True)

		self.assertEqual(len(self.session[settings.CART_SESSION_ID]), 0)
		self.assertEqual(response_3.status_code, 200)

	def test_rent_object_is_created_on_checkout(self):
		url_1 = reverse('book_details',kwargs={'book_id':self.book_1.id})
		data_1 = {'start_date':date.today(),'end_date':date.today()+timedelta(days=5)}
		response_1 = self.client.post(url_1, data_1, follow=True)
		
		url_2 = reverse('book_details',kwargs={'book_id':self.book_2.id})
		data_2 = {'start_date':date.today()+timedelta(days=2),'end_date':date.today()+timedelta(days=5)}
		response_2 = self.client.post(url_2, data_2, follow=True)

		url_3 = reverse('checkout')
		response_3 = self.client.get(url_3, follow=True)

		self.assertEqual(Rent.objects.all().count(), 1)
		self.assertEqual(response_3.status_code, 200)

	def test_rentitem_object_is_created_on_checkout(self):
		url_1 = reverse('book_details',kwargs={'book_id':self.book_1.id})
		data_1 = {'start_date':date.today(),'end_date':date.today()+timedelta(days=5)}
		response_1 = self.client.post(url_1, data_1, follow=True)
		
		url_2 = reverse('book_details',kwargs={'book_id':self.book_2.id})
		data_2 = {'start_date':date.today()+timedelta(days=2),'end_date':date.today()+timedelta(days=5)}
		response_2 = self.client.post(url_2, data_2, follow=True)

		url_3 = reverse('checkout')
		response_3 = self.client.get(url_3, follow=True)

		self.assertEqual(RentItem.objects.all().count(), 2)
		self.assertEqual(response_3.status_code, 200)
