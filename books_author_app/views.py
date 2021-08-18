from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    print("*"*40)
    print("Index render")
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', context)

def book_info(request, book_id):
    print('*'*40)
    print("Book info page")
    context = {
        'books' : Book.objects.get(id = book_id),
        'authors' : Book.objects.get(id = book_id).authors.all(),
        'all_authors' : Author.objects.all(),
    }
    return render(request, "book_info.html", context)

def append_authors(request, book_id):
    print('*'*40)
    print("Append author page")
    option = Author.objects.get(id = request.POST['select_author'])
    Book.objects.get(id = book_id).authors.add(option)
    return redirect(f'/book_info/{book_id}')

def add_book(request):
    print("*"*40)
    print("Create new book")
    new_book = Book.objects.create(title = request.POST['title'], desc = request.POST['description'])
    return redirect('/')

def authors(request):
    print("*"*40)
    print("Authors render")
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, "authors.html", context)

def add_author(request):
    print("*"*40)
    print("Create author")
    new_author = Author.objects.create(
        first_name = request.POST['first_name'], 
        last_name = request.POST['last_name'], 
        notes = request.POST['notes']
    )
    return redirect('/authors')

def author_info(request, author_id):
    print('*'*40)
    print("Author info page")
    context = {
        'authors' : Author.objects.get(id =  author_id),
        'books' : Author.objects.get(id = author_id).books.all(),
        'all_books' : Book.objects.all(),
    }
    print(context)
    return render(request, "author_info.html", context)

def append_books(request, author_id):
    option = Book.objects.get(id = request.POST['select_book'])
    Author.objects.get(id = author_id).books.add(option)
    return redirect(f'author_info/{author_id}')