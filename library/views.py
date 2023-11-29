from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Book, User, BorrowReturn

class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'  # Replace with your actual template

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'  # Replace with your actual template

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'  # Replace with your actual template

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'  # Replace with your actual template

class UserListView(ListView):
    model = User
    template_name = 'library/user_list.html'  # Replace with your actual template

class UserDetailView(DetailView):
    model = User
    template_name = 'library/user_detail.html'  # Replace with your actual template

class BorrowReturnListView(ListView):
    model = BorrowReturn
    template_name = 'library/borrowreturn_list.html'  # Replace with your actual template

class BorrowReturnDetailView(DetailView):
    model = BorrowReturn
    template_name = 'library/borrowreturn_detail.html'  # Replace with your actual template

