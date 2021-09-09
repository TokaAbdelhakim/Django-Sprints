from books.models import Category
from django.urls import path
from .views import delete_bulk, home, list_categoery, read, index, create_book, save_book, edit_book, delete_book,save_edit, list_categoery
urlpatterns = [
    path('list', home, name='book-list'),
    path('read', read),
    path('', index),
    path('create', create_book, name='create-book'),
    path('save', save_book, name='save-book'),
    path('edit/<book_id>', edit_book, name='edit-book'),
    path('saveEdit/<book_id>', save_edit , name='save-edit'),
    path('delete/<book_id>', delete_book, name='delete-book'),
    path('deleteBulk/', delete_bulk, name='delete-bulk'),
    path('cat/',list_categoery.as_view(), name='catView')
]
