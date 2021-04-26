from django.db import models

class Book(models.Model):
    branch_choices = (
        ('computer_engineering','Computer Engineering'),
        ('IT','I.T.'),
        ('electronics and telecommunication','Electronics and Telecommunication')
    )
    
    title = models.CharField(max_length=50,blank=True)
    author = models.CharField(max_length=50,blank=True)
    edition = models.CharField(max_length=50,blank=True)
    branch = models.CharField(max_length=50,blank=True,choices=branch_choices)
    book_pdf = models.FileField(upload_to='books/pdfs/')
    description = models.TextField(max_length=500,blank=True)
    image = models.ImageField(default='default.png', upload_to='books/images/')
    uploaded_on = models.DateTimeField(auto_now_add =True)
 
    def __str__(self):
        return self.title
