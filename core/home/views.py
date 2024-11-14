from django.shortcuts import render
from home.models import User
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    return render(request, 'pages/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if user exists
        user = User.objects.filter(email=email)
        if user.exists():
            user = user.first()
            if user.check_password(password):
                return redirect('custom_admin_dashboard')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        else:
            messages.error(request, 'User does not exist')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        else:
            # Create the user
            user = User.objects.create_user(name=name, email=email, password=password)
            user.save()
            messages.success(request, 'You are now registered and can log in')
            return redirect('login')
    else:
        return render(request, 'pages/register.html')