from django.shortcuts import render, redirect
from .models import Book, Ticket
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

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

def redirect_home(request):
    return redirect('/home')

def ticket_submit(request):
    name = request.POST['name']
    book = request.POST['book']
    author = request.POST['author']
    description = request.POST['description']

    ticket = Ticket(name=name,book=book,author=author,description=description)

    ticket.save()

    return HttpResponseRedirect('/home')
    
