from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Book, Category
from django.views.generic import ListView

# Create your views here.

def home(request):
    # list books from DB
    books = Book.objects.all()
    #books = Book.objects.filter(isHome=1)
    # render books on the thml page
    return render(request, 'book/index.html', {
        'all_books' : books
    })
    # return HttpResponse('Hello from Books index page')


def read(request):
    return HttpResponse('Hello from Read page.')


def index(request):
    books = Book.objects.all()
    return render(request, 'home/index.html', {
        'all_books' : books
    })

def create_book(request):
    return render(request, 'book/create.html')

def save_book(request):
    # validate request method : POST 
    if request.method == "POST":
        # request.GET
        # print(request.POST)
        book_name = request.POST.get('book_name')
        book_description = request.POST.get('book_desc')
        book_price = request.POST.get('book_price')
        if len(request.FILES) != 0:
            book_photo = request.FILES['book_photo'] 
            print (book_photo)
        else:
            book_photo = request.FILES.get('no')
        isHome = 1 if ('view' in request.POST ) else 0
        # validate against 
        check = is_valid(book_name,book_description,float(book_price))
        # save valid data to the database
        if (check):
            Book.objects.create(
                name=book_name, 
                description=book_description,
                price=book_price,
                isHome = isHome,
                photo=book_photo             
            )
            
            return redirect('book-list')

    return HttpResponse('invalid request')



def edit_book(request, book_id):
    # get book old data from db:
    book = Book.objects.get(pk=book_id)
    #book_photo = request.FILES['book_photo'].open('w+')
    #text = request.FILES['book_photo'].read()
    return render(request, 'book/edit.html', {
        'book_data' : book
        
    })

def save_edit(request, book_id):
    book_name = request.POST.get('book_name')
    book_description = request.POST.get('book_desc')
    book_price = request.POST.get('book_price')
    if len(request.FILES) != 0:
        book_photo = request.FILES['book_photo'] 
    else:
        book_photo = request.FILES.get('no')
    isHome = 1 if ('view' in request.POST ) else 0
    check = is_valid(book_name, book_description, book_price)
    if (check):
        Book.objects.filter(pk=book_id).update(
            name=book_name, 
            description=book_description,
            price=book_price,
            photo=book_photo,
            isHome = int(isHome)
        )    
        return redirect('book-list')
    return HttpResponse('invalid updates')

#validation function
def is_valid(name, desc, price):
    if (name.isdecimal()):
        return False
    if (desc.isdecimal()):
        return False
    if ( float(price) <= 0):
        return False
    return True

def delete_book(request, book_id):
    Book.objects.get(pk=book_id).delete()
    return redirect('book-list')

# Bulk delete 
def delete_bulk(request):
    group_ids = request.POST.getlist('book_id[]')
    for id in group_ids:
        Book.objects.get(pk=id).delete()
    return redirect('book-list')

class list_categoery (ListView):
    template_name= 'book/cat.html'
    model = Category
    context_object_name = 'categories'