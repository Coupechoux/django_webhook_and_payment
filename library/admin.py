from django.contrib import admin
from .models import Book, Author, Shelf

# Register your models here
class BookAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'author')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Shelf)
