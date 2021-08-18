from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('book_info/<int:book_id>', views.book_info),
    path('book_info/<int:book_id>/append_authors', views.append_authors),
    path('add_book', views.add_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('author_info/<int:author_id>', views.author_info),
    path('author_info/<int:author_id>/append_books', views.append_books),
]




