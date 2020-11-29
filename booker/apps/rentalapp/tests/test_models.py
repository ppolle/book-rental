from django.test import TestCase, RequestFactory
from booker.apps.rentalapp.models import Rent, RentItem
from booker.apps.libraryapp.models import Book, BookType
from datetime import date, timedelta

class RentalAppModelTests(TestCase):
	def setUp(self):
		self.novel_1 = BookType.objects.create(name='novel', daily_rate=1.50)
		self.fiction_2 = BookType.objects.create(name='fiction', daily_rate=3.00)
		self.regular_3 = BookType.objects.create(name='regular', daily_rate=1.50)
		
		self.book_3 = Book.objects.create(title='A man of the people',description='A novel by chinua achebe about a man of the people.', genre=self.novel_1)
		self.book_4 = Book.objects.create(title='Drunk', description='A book by Steve Biko about a man struggling with his drinking demons', genre=self.fiction_2)
		self.book_5 = Book.objects.create(title='Green Belt', description='A book about conservation of forests', genre=self.regular_3)
	
	def test_rent_object_creation(self):
		rent = Rent.objects.create(total=10.0)
		rent.items.add(self.book_3)
		rent.save()

		self.assertEqual(Rent.objects.all(), 1)
		self.assertEqual(rent.total,10.0)

	def test_rent_item_creation(self):
		start_date = date.today()+timedelta(days=2)
		end_date = date.today()+timedelta(days=7)
		
		rent = Rent.objects.create(total=15.00)
		rent.items.add(self.book_4)
		rent.save()

		item = RentItem.objects.create(rent=rent, 
			book=self.book_4, 
			start_date=start_date, 
			stop_date=end_date)

		self.assertEqual(RentItem.objects.all(), 1)
