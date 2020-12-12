from django import forms
from datetime import date, timedelta
from booker.apps.rentalapp.models import RentItem
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
	input_type = 'date'

class RentBookForm(forms.Form):
	book_id = forms.IntegerField(widget=forms.HiddenInput)
	start_date = forms.DateField(widget=DateInput)
	end_date = forms.DateField(widget=DateInput)

	def date_rage_dates(self, date1, date2):
		delta = date2-date1
		return set([date1 + timedelta(days=i) for i in range(delta.days + 1)])

	def clean_start_date(self):
		now = date.today()
		if self.cleaned_data['start_date'] < now:
			raise forms.ValidationError('The start date cannot be in the past')

		return self.cleaned_data['start_date']

	def clean_end_date(self):
		if self.cleaned_data['end_date'] < date.today():
			raise forms.ValidationError('This date cannot be in the past')

		if self.cleaned_data['start_date'] > self.cleaned_data['end_date']:
			raise forms.ValidationError('End date can only come after start date')

		return self.cleaned_data['end_date']

	def clean(self):
		book_id = self.cleaned_data['book_id']
		if  RentItem.objects.filter(book__id=book_id).exists():
			rent_item = RentItem.objects.filter(book__id=book_id).last()
			new_dates = self.date_rage_dates(self.cleaned_data['start_date'], self.cleaned_data['end_date'])
			old_dates = self.date_rage_dates(rent_item.start_date, rent_item.stop_date)

			if not new_dates.isdisjoint(old_dates):
				dates = new_dates & old_dates
				date_strings = map(lambda x:x.strftime('%d/%m/%Y'), sorted(dates))
				error_msg = 'The book is already booked on the following dates: {} Please choose alternative dates'.format(', '.join(date_strings))
				raise forms.ValidationError(error_msg)
		
