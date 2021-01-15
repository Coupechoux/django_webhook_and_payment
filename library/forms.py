from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class BookForm(forms.Form):
	title = forms.CharField(max_length=200)
	author = forms.CharField(max_length=30, required=False)
	shelf_row = forms.IntegerField(required=False, validators=[MinValueValidator(1), MaxValueValidator(20)])
	shelf_column = forms.IntegerField(required = False, validators=[MinValueValidator(1), MaxValueValidator(10)])
	
class ContactForm(forms.Form):
	name = forms.CharField(max_length=30, required=False, label="Nom ")
	mail = forms.EmailField(required=False, label="Email ")
	
	subject = forms.CharField(max_length=256, label="Sujet ")
	message = forms.CharField(max_length=2048, label="Message ", widget=forms.Textarea)