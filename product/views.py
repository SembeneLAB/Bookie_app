from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def shop(request):
    
    if request.user.is_authenticated:
        # user is logged in
        return render(request, 'shop.html', {})
    else:
        # user is not logged in
        return render(request, 'login:login', {})

