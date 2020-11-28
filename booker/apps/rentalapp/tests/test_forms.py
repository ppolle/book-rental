from django.test import TestCase
from datetime import date, timedelta
from booker.apps.rentalapp.forms import RentBookForm

# Create your tests here.
class RentBookFormTests(TestCase):
	def test_valid_form(self):

		start_date = date.today()
		end_date = start_date+timedelta(days=5)
		
		data={"start_date":start_date,"end_date":end_date}

		form = RentBookForm(data=data)
		self.assertTrue(form.is_valid())

	def test_invalid_form(self):
		start_date = date.today()
		data = {"start_date":start_date}

		form = RentBookForm(data=data)
		self.assertFalse(form.is_valid())		

	def test_earlier_end_date(self):
		start_date = date.today()+timedelta(days=5)
		end_date = date.today()+timedelta(days=1)

		data={"start_date":start_date,"end_date":end_date}
		form=RentBookForm(data=data)
		
		if form.errors.items():
			error = dict(form.errors.items())
			self.assertTrue(error['end_date'][0], 'End date can only come after start date')
		self.assertFalse(form.is_valid())