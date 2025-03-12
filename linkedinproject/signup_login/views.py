from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password") 
        user_obj = User.objects.get(email=email)
        users = authenticate(request, username=user_obj.username, password=password)

        if users is not None:
            login(request, users)
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password!")
            return redirect('login')

    return render(request, "login.html")


def signup(request):    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Your password does not match")
            return redirect("signup")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email already exists, please try with the different email address!")
            return redirect("signup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"This username already exists, please try with different username")
            return redirect("signup")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account successfully created!!")
        return redirect("login")
    return render(request, "signup.html")

def home(request):
    return render(request, "home.html")

