from django.shortcuts import render, redirect
from .models import Transaction, User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
  transactions = Transaction.objects.filter(user=request.user)
  transactions = [transaction.to_dict() for transaction in transactions]
  context = {'transactions': transactions}
  return render(request, 'home.html', context)

def deposit(request):
  if request.method == 'POST':
    user = request.user
    user_balance = user.balance

    try:
      transaction_value = float(request.POST.get('value'))
    except:
      messages.error(request, 'Please input a valid positive number')
      return redirect('home')

    user.balance = user_balance + transaction_value
    user.save()

    transaction = Transaction.objects.create(
      user = request.user,
      transaction_type = 'dep',
      value = transaction_value
    )

    return redirect('home')

  return redirect('home')

def withdraw(request):
  if request.method == 'POST':
    user = request.user
    user_balance = user.balance

    try:
      transaction_value = float(request.POST.get('value'))
    except:
      messages.error(request, 'Please input a valid positive number')
      return redirect('home')

    if (user_balance < transaction_value):
      messages.error(request, 'Your balance is not enough')
      return redirect('home')

    user.balance = user_balance - transaction_value
    user.save()

    transaction = Transaction.objects.create(
      user = request.user,
      transaction_type = 'wit',
      value = transaction_value
    )

    return redirect('home')

  return redirect('home')

def login(request):
  if request.user.is_authenticated:
    return redirect('home')

  if request.method == 'POST':
    username = request.POST.get('username').lower()
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'User does not exist')
      return redirect('login')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      auth_login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'Wrong password!')
      return redirect('login')

  return render(request, 'login_register.html')

def register(request):
  if request.method == 'POST':
    full_name = request.POST.get('full_name')
    username = request.POST.get('username').lower()
    email = request.POST.get('email')
    password = request.POST.get('password')

    if User.objects.filter(username=username).exists():
      messages.error(request, 'User with that username already exists')
      return redirect('register')
    
    user = User.objects.create_user(username=username,
                                  email=email,
                                  password=password,
                                  name=full_name)
    
    auth_login(request, user)
    return redirect('home')

  return render(request, 'login_register.html')

def logout(request):
    auth_logout(request)
    return redirect('home')