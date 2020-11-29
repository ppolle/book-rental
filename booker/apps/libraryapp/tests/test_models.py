from django.test import TestCase
from datetime import date, timedelta
from booker.apps.libraryapp.model import Book, BookType

class LibraryAppTests(TestCase):
	def test_book_type_creation():
		novel_type = BookType.objects.create(name='novel',daily_rate=1.50)
		fiction_type = BookType.objects.create(name='fiction', daily_rate=3.00)

		self.assertEqual(BookType.objects.all().count(), 2)
		self.assertEqual(novel_type.name, 'novel')

	def test_book_creation(self):
		novel = BookType.objects.create(name='novel',daily_rate=1.50)
		book = Book(title='a man of the people', genre=novel, description='A man popular among men')

		self.assertEqual(Book.objects.all().count(), 1)

	def test_calculate_cost(self):
		novel = BookType.objects.create(name='novel',daily_rate=1.50)
		book = Book(title='a man of the people', genre=novel, description='A man popular among men')

		start_date = date.today()
		stop_date = date.today()+timedelta(days=3)

		cost = book.test_calculate_cost(start_date, stop_date)
		self.assertEqual(cost,4.5)


