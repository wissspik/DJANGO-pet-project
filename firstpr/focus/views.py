from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Url,Text
import uuid


def articles_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:  # Убедитесь, что пользователь вошёл в систему
            return redirect('home')  # Перенаправьте на страницу логина, если он анонимный
        url_post = uuid.uuid4().hex
        text = request.POST.get('article_text')
        title = request.POST.get('article_title')
        title_2 = request.POST.get('article_subtitle')
        if request.POST.get('choice') == 'yes':
            anonymity = True
        else:
            anonymity = False
        # Создаем объект Url и сохраняем его в переменной new_url
        new_url = Url.objects.create(user=request.user, url=url_post)

        # Создаем объект Text, передавая в поле url именно объект new_url, а не строку
        Text.objects.create(url=new_url, anonymity=anonymity, text=text, title=title, subtitle=title_2)

        return redirect('focus_p')  # Перенаправляем после успешной отправки
    return render(request, 'articles.html')

def urls_view(request, url):
    pattern = get_object_or_404(Text, url__url=url)
    return render(request,'article_detail.html',{'article': pattern})

def focus_list_view(request):
    url_instances = Url.objects.filter(user=request.user)  # корректно
    return render(request, 'url_art.html', {'article': url_instances})

