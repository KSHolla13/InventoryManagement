from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import book
from .forms import BookForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user_model
#User = get_user_model()
from users_app.models import CustomUser

def Reader(request):
    context = {
        'welcome_text' : 'Reader',
    }
    return render (request, 'Reader.html', context)


def collection(request):
    all_books = book.objects.all()
    paginator = Paginator(all_books, 7)
    page = request.GET.get('pg')
    all_books = paginator.get_page(page)
   
    return render (request, 'collection.html', {'all_books': all_books})


@login_required
def home(request):
    all_books = book.objects.filter(manage = request.user)
    paginator = Paginator(all_books, 6)
    page = request.GET.get('pg')
    all_books = paginator.get_page(page)
    return render (request, 'home.html', {'all_books': all_books})

@login_required
def delete_book(request, id):
    Book = book.objects.get(pk=id)
    if Book.manage == request.user:
        Book.delete()
    else :
        messages.error(request,("Access Restricted"))    
    return redirect('home')

@login_required
def  edit_book(request, id):
    if request.method == "POST":
        Book = book.objects.get(pk=id)
        form = BookForm(request.POST or None, instance = Book)
        if form.is_valid():
            #form.save(commit=False).manage = request.user
            form.save()
        messages.success(request,("Book Edited"))   
        return redirect ('home')    
    else:
        book_obj = book.objects.get(pk=id)
        return render (request, 'edit.html', {'book_obj':book_obj})      
    

def contact(request):
    context = {
        'welcome_text' : 'contact',
    }
    return render (request, 'contact.html', context)

@login_required
def Addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form is not None :  
          if form.is_valid():
            form.save(commit=False).manage = request.user
            form.save()
            messages.success(request,("New book added"))   
            return redirect ('home')   
        else :
            return redirect('register') 
    else:
       return render (request, 'Addbook.html', {})    


def storelist(request):
    all_stores = CustomUser.objects.all()
    paginator = Paginator(all_stores, 7)
    page = request.GET.get('pg')
    all_stores = paginator.get_page(page)
   
    return render (request, 'storelist.html', {'all_stores': all_stores})       