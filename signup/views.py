from django.shortcuts import render , redirect

from .models import user
from .forms import SignUpForm
from django.contrib.auth import login

def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST) 

        if form.is_valid():
            form.save()  
            return redirect('home')
    else:
        form = SignUpForm(initial={'email':'@gmail.com', 'username':request.user.username}) 
    return render(request, 'signup/index.html', {'form': form})
