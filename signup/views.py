from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Succesful'))
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup/index.html', {'form': form})