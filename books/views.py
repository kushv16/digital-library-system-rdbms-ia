from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

@login_required
def home(request):
    return render(request, 'books/home.html')

@login_required
def about(request):
    return render(request, 'books/about.html')

@login_required
def search_books(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__icontains = searched)
        content = {
            'searched': searched,
            'books': books,
            'totalbooks': books.count
        }
        return render(request, 'books/book_search.html', content)