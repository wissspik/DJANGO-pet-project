from .models import Person
from django.shortcuts import render, redirect
from django.contrib import messages

def entrance_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            user = Person.objects.get(name=name)  # Используем модель Person
        except Person.DoesNotExist:
            messages.error(request, "Данного логина не существует. Пройдите регистрацию")
            return redirect('home')
        if password == user.password:

            return redirect('focus_p')
        else:
            messages.error(request, "Пароли не совпадают")
    return render(request, 'entrance.html')

def registration_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password_1 = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        exists = Person.objects.filter(name=name).exists()  # Проверяем, существует ли пользователь с таким именем
        if exists:
            messages.error(request, "Данный ник уже существует")
        else:
            if password_1 == password_2:  # Проверка на совпадение паролей
                Person.objects.create(name=name, password=password_1)
                messages.add_message(request, messages.SUCCESS, "Вы успешно зарегистрировались", extra_tags='success')
            else:
                messages.error(request, "Пароли не совпадают")
    return render(request, 'registration.html')

def focus_view(request):
    return render(request, 'focus.html')

