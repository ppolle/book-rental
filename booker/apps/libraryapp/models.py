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
		dates_elapsed = stop_date-start_date
		days_elapsed = dates_elapsed.days

		if self.genre.minimum_days==0 and self.genre.early_rates==0:
			rent_cost = self.genre.daily_rate*days_elapsed
		elif self.genre.minimum_days>0 and self.genre.early_rates==0:
			minimum_rent=self.genre.minimum_days*self.genre.daily_rate
			if days_elapsed <= self.genre.minimum_days:
				rent_cost = minimum_rent
			else:
				rent_cost = days_elapsed*self.genre.daily_rate
		else:
			minimum_rent=self.genre.minimum_days*self.genre.early_rates
			if days_elapsed<=self.genre.minimum_days:
				rent_cost=minimum_rent
			else:
				normal_rent = (days_elapsed-self.genre.minimum_days)*self.genre.daily_rate
				rent_cost=minimum_rent+normal_rent

		return rent_cost

class BookType(models.Model):
	'''
	Holds all Book Type Information
	'''
	name = models.CharField(max_length=1000)
	daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
	early_rates = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	minimum_days = models.PositiveIntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

