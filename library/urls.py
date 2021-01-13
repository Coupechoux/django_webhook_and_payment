from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='library_index'),
	path('list/', views.list_books, name='list_books'),
	path('add-book', views.add_book, name='add_book'),
]