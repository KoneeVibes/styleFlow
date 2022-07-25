from django.shortcuts import render , redirect

from signup.models import user
from .forms import SignUpForm
from django.contrib.auth import login

def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST) 

        if form.is_valid():
            user = form.save()
            login(request, user) ##the error message is caused by this line.
            return redirect('home')
    else:
        form = SignUpForm(initial={'email':'@gmail.com'}) 
    return render(request, 'signup/index.html', {'form': form})


