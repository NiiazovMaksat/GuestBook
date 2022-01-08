from django.shortcuts import render, redirect, get_object_or_404

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

def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'GET':
        form = BookForm(initial={
            'name': book.name,
            'email': book.email,
            'text': book.text,})

        return render(request, 'edit.html', {'book': book, 'form': form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.name = form.cleaned_data.get('name')
            book.email = form.cleaned_data.get('email')
            book.text = form.cleaned_data.get('text')
            book.save()
            return redirect("main")
        return render(request, 'edit.html', {'book': book, 'form': form})

def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'book': book})
    else:
        book.delete()
        return redirect("main")
