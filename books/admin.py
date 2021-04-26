from django.contrib import admin
from .models import Book,Ticket

class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'author', 'id', 'edition', 'branch', 'uploaded_on']

class AdminTicket(admin.ModelAdmin):
    list_display = ['name','book','author']

admin.site.register(Book, AdminBook)
admin.site.register(Ticket,AdminTicket)