from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from .models import Url,Text,Comment
import uuid

def logout_view(request):
    logout(request)
    return redirect('home')  # Замените 'home' на имя URL, куда нужно перенаправить пользователя после выхода.

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
    comments = pattern.comments.all()
    if request.method == 'POST':
        content = request.POST.get('comment')
        time = request.POST.get('timezone')
        s = Text.objects.get(url__url=url)  # ищем по полю url связанной модели Url
        Comment.objects.create(post = s,user =request.user,content = content ,created_at = time)
    return render(request,'article_detail.html',{'article': pattern,'url': url,'comments':comments})

def focus_list_view(request):
    url_instances = Url.objects.filter(user=request.user)
    return render(request, 'url_art.html', {'article': url_instances})

def focus_popular_view(request):
    return render(request,'focus_popular.html')


