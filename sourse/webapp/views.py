from django.shortcuts import render, redirect

# Create your views here.
from webapp.forms import BookForm
from webapp.models import Book


def main_page(request):
    book = Book.objects.order_by('updated_at')
    return render(request, 'main_page.html',{'book': book})
def create(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            new_book = Book.objects.create(name=name, email=email, text=text)
            return redirect("main")

        return render(request, 'create.html', {'form': form})