from django.shortcuts import render
from django.views import View
from .models import Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            'books': books
        }

        return render(request, 'library/book_list.html', context)


