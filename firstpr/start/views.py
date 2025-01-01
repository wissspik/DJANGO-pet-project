from django.shortcuts import render,redirect
from argon2 import PasswordHasher
from .models import Person

from django.shortcuts import render, redirect
from argon2 import PasswordHasher
from .models import Person

def d_view(request):
    ph = PasswordHasher()

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            # Пытаемся найти пользователя по имени
            person = Person.objects.get(name=name)

            # Проверяем пароль
            if ph.verify(person.password, password):  # Сравнение пароля
               return redirect('secret')  # Если пароль совпадает, перенаправляем
            else:
                ### банер с сообщение о неправильном пароле
               return redirect('home')

        except Person.DoesNotExist:
            ### банер с предложение о регистрации
            pass
    return render(request,'d.html')
def registration_view(request):





    # Если метод GET, отображаем форму
    return render(request, 'd.html')
def registration_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password_1 = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        exists = Person.objects.filter(name=name).exists() # истинность нахождения users в бд
        if exists:
            return redirect('home') # пользователь есть
        #else:
         #   if password_1 == password_2: # верность введения двух паролей
          #  else:




    return render(request,'registration.html')


