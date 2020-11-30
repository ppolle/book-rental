from django.test import TestCase
from datetime import date, timedelta
from booker.apps.libraryapp.models import Book, BookType

class LibraryAppTests(TestCase):
	def test_book_type_creation(self):
		novel_type = BookType.objects.create(name='novel',daily_rate=1.50)
		fiction_type = BookType.objects.create(name='fiction', daily_rate=3.00)

		self.assertEqual(BookType.objects.all().count(), 2)
		self.assertEqual(str(novel_type), 'novel')
		self.assertIsInstance(novel_type.name, str)

	def test_book_creation(self):
		novel = BookType.objects.create(name='novel',daily_rate=1.50)
		book = Book.objects.create(title='a man of the people', genre=novel, description='A man popular among men')

		self.assertEqual(Book.objects.all().count(), 1)
		self.assertEqual(str(book),book.title)

	def test_calculate_cost(self):
		novel = BookType.objects.create(name='novel',daily_rate=1.50)
		book = Book(title='a man of the people', genre=novel, description='A man popular among men')

		start_date = date.today()
		stop_date = date.today()+timedelta(days=3)

		cost = book.calculate_cost(start_date, stop_date)
		self.assertEqual(cost,4.5)

	def test_calculate_cost_with_minimal_days(self):
		novel = BookType.objects.create(name='novel', daily_rate=1.0,minimum_days=3)
		book = Book(title='a man of the people', genre=novel, description="A man's people")
		start_date = date.today()
		stop_date = date.today()+timedelta(days=6)
		cost = book.calculate_cost(start_date, stop_date)
		self.assertEqual(cost,6)

	def test_calculate_cost_with_total_days_more_than_minimal_days(self):
		novel = BookType.objects.create(name='novel', daily_rate=1.0,minimum_days=3)
		book = Book(title='a man of the people', genre=novel, description="A man's people")
		start_date = date.today()
		stop_date = date.today()+timedelta(days=5)
		cost = book.calculate_cost(start_date, stop_date)
		self.assertEqual(cost,5)

	def test_calculate_cost_with_minimal_days_and_early_rates(self):
		novel = BookType.objects.create(name='novel', daily_rate=2.0,minimum_days=3, early_rates=1)
		book = Book(title='a man of the people', genre=novel, description="A man's people")
		start_date = date.today()
		stop_date = date.today()+timedelta(days=1)
		cost = book.calculate_cost(start_date, stop_date)
		self.assertEqual(cost,3)

	def test_calculate_cost_with_minimal_days_and_early_rates_with_more_days(self):
		novel = BookType.objects.create(name='novel', daily_rate=2.0,minimum_days=3, early_rates=1)
		book = Book(title='a man of the people', genre=novel, description="A man's people")
		start_date = date.today()
		stop_date = date.today()+timedelta(days=5)
		cost = book.calculate_cost(start_date, stop_date)
		self.assertEqual(cost,7)