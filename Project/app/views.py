from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Books
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer

# Create your views here.

class Another(View):
    output = '';
    # all data with filter
    # books = Books.objects.filter(is_published=True);
    # for book in books:
    #     output += f"{book.title}|"
    #
    # output += f"we have {len(books)} books"
    # get data from condition
    book = Books.objects.get(id=2);
    output = f"we have {book.title} book"

    def get(self,request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('hello')

def temp(request):
    # all data
    books = Books.objects.all()
    return render(request,'first_temp.html',{'books':books,'data':'this id list of books'})


# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
