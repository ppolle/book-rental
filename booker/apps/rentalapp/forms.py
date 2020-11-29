from django import forms
from django.core.exceptions import ValidationError
from datetime import date

class DateInput(forms.DateInput):
	input_type = 'date'

class RentBookForm(forms.Form):
	start_date = forms.DateField(widget=DateInput)
	end_date = forms.DateField(widget=DateInput)

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