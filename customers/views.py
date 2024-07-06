from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Customer

def accounts(request):
    context = {}
    if request.method == 'POST':
        if 'register' in request.POST:
            context['register'] = True
            try:
                username = request.POST.get("name")
                email = request.POST.get('email')
                password = request.POST.get('password')
                address = request.POST.get('address')
                phone = request.POST.get('phone')

                # Check for existing user with the same username or email
                if User.objects.filter(username=username).exists():
                    raise Exception('Username already exists')
                if User.objects.filter(email=email).exists():
                    raise Exception('Email already exists')

                # Create user
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)  # Hash the password
                user.save()

                # Create customer
                customer = Customer.objects.create(user=user, phone=phone, address=address)
                
                # Redirect to home page after successful registration
                success_messages = 'user registered successfully'
                messages.success(request, success_messages)
                return redirect('home')
            except Exception as e:
                error_message = str(e)
                messages.error(request, error_message)

        elif 'login' in request.POST:
            context['register'] = False
            username = request.POST.get("name")
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')

    return render(request, 'account.html', context)

def signout(request):
    logout(request)
    return redirect('home')