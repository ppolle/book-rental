from django.db import models
from booker.apps.libraryapp.models import Book

# Create your models here.

class Rent(models.Model):
	'''
	Hold information regarding a single rent transaction
	'''
	items = models.ManyToManyField(Book, through="RentItem")
	total = models.DecimalField(max_digits=50, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.id
	
	class Meta:
		ordering = ['-timestamp']

class RentItem(models.Model):
	'''
	Hold the details about each book in a single rent transaction
	'''
	rent = models.ForeignKey("Rent", on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	start_date = models.DateField()
	stop_date = models.DateField()

	def __str__(self):
		return self.id


