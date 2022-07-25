from django.shortcuts import redirect, render
from .forms import logindetails


def login(request):
    if request.method == 'POST':  
        form = logindetails(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = logindetails(initial={'username':request.user.username, 'email':request.user.email})
    return render(request, 'login/login.html', {'form': form})
