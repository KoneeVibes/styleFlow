from django.urls import path
from . import views

urlpatterns = [
    path('signout/', views.logout, name = 'signout')
]