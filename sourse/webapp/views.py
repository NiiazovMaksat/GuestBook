from django.shortcuts import render

# Create your views here.
from webapp.models import Book


def main_page(request):
    book = Book.objects.order_by('updated_at')
    return render(request, 'main_page.html',{'book': book})