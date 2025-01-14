<<<<<<< HEAD
from django.shortcuts import render,redirect
from argon2 import PasswordHasher
from .models import Person

from django.shortcuts import render, redirect
from argon2 import PasswordHasher
from .models import Person
=======
from django.shortcuts import render, redirect
from argon2 import PasswordHasher
from django.contrib import messagesmodels import Person
>>>>>>> ec4bec4 (/)

def d_view(request):
    ph = PasswordHasher()

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        try:
            # Пытаемся найти пользователя по имени
            person = Person.objects.get(name=name)
<<<<<<< HEAD

=======
>>>>>>> ec4bec4 (/)
            # Проверяем пароль
            if ph.verify(person.password, password):  # Сравнение пароля
               return redirect('secret')  # Если пароль совпадает, перенаправляем
            else:
                ### банер с сообщение о неправильном пароле
               return redirect('home')

        except Person.DoesNotExist:
            ### банер с предложение о регистрации
            pass
<<<<<<< HEAD
    return render(request,'d.html')
def registration_view(request):





    # Если метод GET, отображаем форму
    return render(request, 'd.html')
def registration_view(request):
=======
    return render(request,'entrance.html')
def registration_view(request):
    ph = PasswordHasher()
>>>>>>> ec4bec4 (/)
    if request.method == 'POST':
        name = request.POST.get('name')
        password_1 = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        exists = Person.objects.filter(name=name).exists() # истинность нахождения users в бд
        if exists:
<<<<<<< HEAD
            return redirect('home') # пользователь есть
        #else:
         #   if password_1 == password_2: # верность введения двух паролей
          #  else:




    return render(request,'registration.html')


=======
            messages.add_message(request,messages.WARNING, "Данный ник уже существует",extra_tags = 'error_users')
        else:
            if password_1 == password_2: # верность введения двух паролей
                Person.objects.create(name = name,password = ph.hash(password_1))
                messages.add_message(request,messages.SUCCESS,"Вы успешно зарегистировались",extra_tags = 'success')

            else:
                messages.add_message(request, messages.ERROR, "Пароли не совпадают", extra_tags='error_password')
    return render(request,'registration.html')
def focus_view(request):
    return True
>>>>>>> ec4bec4 (/)
