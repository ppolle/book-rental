from django import forms

class RentBookForm(forms.Form):
	start_date = forms.DateField()
	end_date = forms.DateField()