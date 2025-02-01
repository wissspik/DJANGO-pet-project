from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Url,Text
import uuid


def articles_view(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:  # Убедитесь, что пользователь вошёл в систему
            return redirect('home')  # Перенаправьте на страницу логина, если он анонимный
        url_post = uuid.uuid4().hex
        full_url = f'/focus/articles/{url_post}/'
        Text = request.POST.get('article_text')
        Title = request.POST.get('article_title')
        Title_2 = request.POST.get('article_subtitle')

        # Создаём запись с привязкой к текущему пользователю
        Text.objects.create(
            user=request.user,
            TXT_Text=Text,
            TXT_title=Title,
            TXT_subtitle=Title_2
        )
        return redirect('focus_p')  # Перенаправляем после успешной отправки
    return render(request, 'articles.html')


def urls_view(request, url):
    link = get_object_or_404(URL, url=f'/focus/articles/{url}/',url_Text =  article_text )

    return render(request, 'urt_art.html', {'url': link.url, 'article_text': article_text})
