from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm

def signup(request): 
    form = UserCreationForm(request.POST) 
    if form.is_valid(): 
        form.save() 
        username = form.cleaned_data.get('username') 
        password = form.cleaned_data.get('password') 
        user = authenticate(username=username, password=password) 
        login(request, user) 
        return redirect('home') 
    context = { 
        'form': form 
    } 
    return render(request, 'signup.html', context) 