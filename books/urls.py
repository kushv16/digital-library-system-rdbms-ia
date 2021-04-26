from django.urls import path
from .views import BookListView, BookDetailView, home, about, search_books, redirect_home,ticket_submit

urlpatterns = [
    path('', redirect_home, name='home'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('books/search', search_books, name='search-books'),
    path('ticket_submitted/', ticket_submit , name='ticket-submit')
]