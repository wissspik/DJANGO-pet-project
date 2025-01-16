from .models import Baners
from django.shortcuts import render, redirect
from django.contrib import messages

def focus_view(request):
    if method.request == 'POST':
        name = request.POST.get('name')
        day = request.POST.get('day')
        time = request.POST.get('time')
        color = request.POST.get('color')

        user = request.user #получаю логин для баннера
        Baners.objects.create(user = user,name=name, day = day,time = time,color = color)

        return redirect('task_view')  # Перенаправляем на страницу с задачами (после добавления)
    return render(request,'focus.html')

def task_view(request):
    # Извлекаем все баннеры для текущего пользователя
    user = request.user  # или получаем пользователя из сессии
    banners = Baners.objects.filter(user=user)  # Получаем баннеры по текущему пользователю

    # Передаем данные в шаблон
    return render(request, 'your_template.html', {'banners': banners})