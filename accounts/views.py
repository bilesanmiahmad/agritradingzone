from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from accounts.models import User
from trades import models as mt
from accounts import constants as ct
from tradingzone.utils import mail

# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            email=request.POST['email'],
            password=request.POST['password'])
        if user is not None:
            if user.is_verified:
                auth.login(request, user)
                return redirect('products')
            else:
                return render(
                    request,
                    'accounts/login.html',
                    {'error': 'Please verify your account from your email.'})
        else:
            return render(
                request, 'accounts/login.html',
                {'error': 'Invalid Credentials'})
    else:
        return render(request, 'accounts/login.html')


def verify(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user:
        user.is_verified = True
        user.save()
        return redirect('login')


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
                profile_data = mt.Profile()
                profile_data.user = user
                profile_data.save()
                auth.login(request, user)
                mail.send_formatted_email(user)
                return redirect('login')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords don\'t match.'})
    else:

        return render(request, 'accounts/signup.html', {'countries': countries, 'language': request.LANGUAGE_CODE})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        auth.logout(request)
        return redirect('home')


@login_required()
def profile(request):
    user = request.user
    bids = mt.Bid.objects.filter(client=user)
    sales = mt.Sale.objects.filter(seller=user)
    try:
        profile_data = mt.Profile.get(user=user)
    except mt.Profile.DoesNotExist:
        profile_data = {}

    return render(request, 'accounts/profile.html', {
        'user': user, 'bids': len(bids),
        'sales': len(sales), 'profile': profile_data})


