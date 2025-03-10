from django.shortcuts import render, redirect

# Create your views here.
def user_login(request):
    return render(request, "login.html")