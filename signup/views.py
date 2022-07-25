from django.shortcuts import render , redirect

from .models import user
from .forms import SignUpForm
from django.contrib.auth import login

def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST) 

        if form.is_valid():
            form.save()  
            return redirect('login')
    else:
        form = SignUpForm(initial={'email':'@gmail.com'}) 
    return render(request, 'signup/index.html', {'form': form})
