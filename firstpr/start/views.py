from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def entrance_view(request):

    if request.method == 'POST':
        name = request.POST.get('name') # получаем пароль и ник
        password = request.POST.get('password')


        if not User.objects.filter(username=name).exists():
            messages.error(request, "Данного логина не существует. Пройдите регистрацию")
            return redirect('home')


        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('focus_p')
        else:
            messages.error(request, "Неверный логин или пароль.")
    return render(request, 'login.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('focus_p')
    else:
        form = UserCreationForm()  # Пустая форма при GET-запросе

    return render(request, 'regis.html', {'form': form})

def focus_view(request):
    return render(request, 'focus.html')

