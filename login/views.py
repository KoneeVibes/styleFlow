from django.shortcuts import redirect, render
from .forms import logindetails
from django.contrib.auth import login, authenticate


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':  
        form = logindetails(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        form = logindetails()
    return render(request, 'login/login.html', {'form': form})
