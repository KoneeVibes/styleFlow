from django.shortcuts import redirect, render
from .forms import logindetails
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':  
        form = logindetails(request.POST)
        if form.is_valid():
            form.save()
            user = form.objects.create_user(
                username = form.cleaned_data['username'], 
                password = form.cleaned_data['password']
            )  
            login(request, user) 
            authenticate(username=request.GET['username'], password=request.GET['password']) 
            if user is not None:
                login(request, user)
            return redirect('home')           
    else:
        form = logindetails()
    return render(request, 'login/login.html', {'form': form})
