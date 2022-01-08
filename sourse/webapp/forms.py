from django import forms
from django.forms import widgets
class BookForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Имя')
    email = forms.CharField(max_length=50, required=True, label='Email')
    text = forms.CharField(max_length=2000, required=False, label='Текст', widget=widgets.Textarea(attrs={'rows':6, 'cols':50}))