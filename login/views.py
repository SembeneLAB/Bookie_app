from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login(request):
   
    if request.method == 'POST':
        # handle the form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('shop:shop')
        else:
            # handle unsuccessful login
            return render(request, 'login.html', {'error': 'Invalid login credentials.'})
    return render(request, 'login.html')
 
