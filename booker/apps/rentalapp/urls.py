"""booker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booker.apps.rentalapp import views
urlpatterns = [
    path('', views.index,name='index'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('book/delete/<int:book_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('clear-cart/', views.clear_cart_items, name='clear_cart'),
   
]
