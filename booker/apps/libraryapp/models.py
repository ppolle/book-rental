from django.db import models
from datetime import date

# Create your models here.

class Book(models.Model):
	'''
	Hold all Book information
	'''
	title = models.CharField(max_length=1000)
	genre = models.ForeignKey("BookType", on_delete=models.CASCADE)
	description = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def calculate_cost(self, start_date, stop_date):
		'''
		Rent a book details
		'''
		today = date.today()
		daily_rate = self.genre.daily_rate
		if start_date and stop_date >= today:
			dates_elapsed = stop_date-start_date
			rent_cost = dates_elapsed.days*daily_rate
		
		return rent_cost

class BookType(models.Model):
	'''
	Holds all Book Type Information
	'''
	name = models.CharField(max_length=1000)
	daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

