from django.shortcuts import redirect, render
from django.contrib import messages
from login_app.models import User
from .models import *

def show_profile(request):
    try:
        request.session['first_name']
        context = {
            'all_books' : Book.objects.all(),
            'liked_books' : User.objects.get(id = request.session['id']).liked_books.all(),
        }
        return render(request, 'show_profile.html', context)
    except:
        return redirect('/')

def upload_book(request):
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        user = User.objects.filter(id = request.session['id'])
        if user: 
            logged_user = user[0]
            uploaded_book = Book.objects.create(title = request.POST['title'],
                        desc = request.POST['desc'],
                        uploaded_by = logged_user)
            logged_user.liked_books.add(uploaded_book)
    return redirect('/books')

def display_book(request, id):
    book = Book.objects.get(id = id)
    context ={
        'book' : book,
        'users_who_like' : book.users_who_like.all(),
        'user' : User.objects.get(id = request.session['id']),
    }
    return render(request, 'book_info.html', context)

def update_book(request, id):
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        book = Book.objects.get(id = id)
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
    return redirect(f'/books/{id}')

def delete_book(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    print('*'*30)
    return redirect('/books')

def add_to_favorites(request, id):
    user = User.objects.filter(id = request.session['id'])
    if user: 
        logged_user = user[0]
        uploaded_book = Book.objects.get(id =id)
        logged_user.liked_books.add(uploaded_book)
    return redirect(f'/books/{id}')

def remove_favoraite(request, id):
    user = User.objects.filter(id = request.session['id'])
    if user: 
        logged_user = user[0]
        uploaded_book = Book.objects.get(id =id)
        logged_user.liked_books.remove(uploaded_book)
    return redirect(f'/books/{id}')

def show_user_profile(request):
    user = User.objects.get(id = request.session['id'])
    context ={
        'user' : user,
        'liked_books' : user.liked_books.all(),
    }
    return render(request, 'user.html', context)