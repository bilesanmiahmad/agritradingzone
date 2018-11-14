from django.shortcuts import render, redirect
from django.contrib import auth
from accounts.models import User
from accounts import constants as ct

# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            email=request.POST['email'],
            password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('products')
        else:
            return render(
                request, 'accounts/login.html',
                {'error': 'Invalid Credentials'})
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    countries = ct.COUNTRIES
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['cemail']
        password = request.POST['password']
        cname = request.POST['cname']
        country = request.POST['country']
        phone = request.POST['phone']

        if request.POST['password'] == request.POST['rpass']:
            try:
                user = User.objects.get(email=request.POST['cemail'])
                return render(
                    request, 'accounts/signup.html',
                    {'error': 'Email already exists.'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    company_name=cname,
                    email=email,
                    phone=phone,
                    country=country,
                    password=password
                )
                auth.login(request, user)
                return redirect('products')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords don\'t match.'})
    else:

        return render(request, 'accounts/signup.html', {'countries': countries})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        auth.logout(request)
        return redirect('home')
