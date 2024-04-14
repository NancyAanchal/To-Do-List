from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages

# Create your views here.
def loginfunc(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print(f"user is {user}")

        if user is not None:
            # Check if the user is active
            if user.is_active:
                # Log in the user
                auth_login(request, user)
                return redirect('tasks')
            else:
                messages.error(request, 'Your account is not active.')

        else:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Incorrect password')
            else:
                messages.error(request, 'This username does not exist')
            return  redirect('login')
    
    else:
        return render(request, 'login/login.html')
    

def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):

    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password==confirm_password:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Account with this email already exists')
                return redirect('register')
            
            else:
                print(f"orginal pwd: {password}")
                hashed_password=make_password(password)
                user = User(username=username, email=email, password=hashed_password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
            
        else:
            messages.info(request,  'Passwords do not match')
            return redirect('register')
    
    else:
        return render(request, "login/register.html")
