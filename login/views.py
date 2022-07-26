from django.shortcuts import redirect, render
from .forms import logindetails
from django.contrib.auth import login


def signin(request):
    if request.method == 'POST':  
        form = logindetails(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup')
    else:
        form = logindetails()
    return render(request, 'login/login.html', {'form': form})
