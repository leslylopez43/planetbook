# from django.urls import path
# from . import views

# app_name = 'library'

# urlpatterns = [
#     path('authors/', views.AuthorListView.as_view(), name='author_list'),
#     path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),

#     path('books/', views.BookListView.as_view(), name='book_list'),
#     path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),

#     path('users/', views.UserListView.as_view(), name='user_list'),
#     path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

#     path('borrowreturns/', views.BorrowReturnListView.as_view(), name='borrowreturn_list'),
#     path('borrowreturns/<int:pk>/', views.BorrowReturnDetailView.as_view(), name='borrowreturn_detail'),

# ]
from django.urls import path
from .views import AuthorListView, BookListView, UserListView, BorrowReturnListView # Import your AuthorListView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('books/', AuthorListView.as_view(), name='book_list'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('borrowreturns/', BorrowReturnListView.as_view(), name='borrowreturn_list'),
    # Add other URL patterns for books, users, and borrow/return as needed
]

