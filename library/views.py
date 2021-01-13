from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import BookForm
from .models import Book, Author, Shelf

# Create your views here.
def index(request):
	# return HttpResponse('Hello')
	return render(request, 'library/index.html')
	
def list_books(request):
	books = Book.objects.all()
	
	return render(request, 'library/books_list.html', {'books':books})
	
def add_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			
			author,created = Author.objects.get_or_create(name=data['author'], defaults={'year':1900})
			shelf,created = Shelf.objects.get_or_create(row=data['shelf_row'], column=data['shelf_column'])
			title = data['title']
			
			Book(title=title, author=author, shelf=shelf).save()
			
			return HttpResponseRedirect(reverse('library_index'))
	else:
		form = BookForm()
		
	return render(request, 'library/book_form.html', {'form':form})