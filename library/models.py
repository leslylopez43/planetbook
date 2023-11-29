from django.db import models

# Table for Authors
class Author(models.Model):
    author_name = models.CharField(max_length=100, null=False)
    biography = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)
    nationality = models.CharField(max_length=50, null=True)

# Table for Books
class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    isbn = models.CharField(max_length=20, null=True)
    genre = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    publication_date = models.DateField(null=True)
    publisher = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=50, null=True)
    num_pages = models.IntegerField(null=True)
    edition = models.CharField(max_length=50, null=True)
    cover_image_url = models.CharField(max_length=255, null=True)

# Table for Users
class User(models.Model):
    member_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    membership_status = models.CharField(max_length=20, null=True)

# Table for Borrowing and Returns
class BorrowReturn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateField(null=True)
    due_date = models.DateField(null=True)
    date_returned = models.DateField(null=True)
    fine = models.DecimalField(max_digits=8, decimal_places=2, null=True)

# Continue defining other models...
