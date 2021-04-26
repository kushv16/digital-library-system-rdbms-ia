from django.contrib import admin
from .models import Book

class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'author', 'id', 'edition', 'branch', 'uploaded_on']

admin.site.register(Book, AdminBook)