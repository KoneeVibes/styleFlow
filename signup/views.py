from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = SignUpForm(request.POST) 

        if form.is_valid():
            form.save()
            username = request.POST['username'] 
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = SignUpForm(initial={'email':'@gmail.com', 'username':request.user.username}) 
    return render(request, 'signup/index.html', {'form': form})

