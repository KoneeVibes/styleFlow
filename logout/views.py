from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout

def logout(request):
    logout(request)
    return HttpResponse("That's it, Bye!")

