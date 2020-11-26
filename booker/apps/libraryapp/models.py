from django.db import models

# Create your models here.

class Book(models.Model):
	'''
	Hold all Book information
	'''
	title = models.CharField(max_length=1000)
	description = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

