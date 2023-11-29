from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),

    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),

    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

    path('borrowreturns/', views.BorrowReturnListView.as_view(), name='borrowreturn_list'),
    path('borrowreturns/<int:pk>/', views.BorrowReturnDetailView.as_view(), name='borrowreturn_detail'),

]
