from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	'''
	Render the index page
	'''
	return render(request, 'rentalapp/index.html')