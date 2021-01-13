from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, blank=True, null=True)
	shelf = models.ForeignKey('Shelf', on_delete=models.CASCADE, blank=True, null=True)
	
	def __str__(self):
		return self.title
	
class Author(models.Model):
	name = models.CharField(max_length=30)
	year = models.IntegerField()
	
	def __str__(self):
		return self.name
	
class Shelf(models.Model):
	row = models.IntegerField()
	column = models.IntegerField()
	
	def __str__(self):
		return f'{self.row}:{self.column}'