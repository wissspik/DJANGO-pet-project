from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from .models import Url,Text,Comment,Like

import uuid
from django.utils import timezone
from django.db.models import Count, Q

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


from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Count, Sum
from .models import Text, Comment, Like


from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Text, Comment, Like

def update_like(post, user, reaction):
    """
    Обновляет или создает объект Like для заданного поста и пользователя.
    Если обнаружены дубликаты, оставляет первый объект и удаляет остальные.
    """
    likes_qs = Like.objects.filter(post=post, user=user)
    if likes_qs.exists():
        like_obj = likes_qs.first()
        like_obj.reaction = reaction
        like_obj.save()
        # Удаляем возможные дубликаты
        """
        duplicates = likes_qs.exclude(pk=like_obj.pk)
        if duplicates.exists():
            duplicates.delete()
        """
    else:
        Like.objects.create(post=post, user=user, reaction=reaction)

def urls_view(request, url):
    # Получаем объект поста по URL
    text_instance = get_object_or_404(Text, url__url=url)
    current_time = timezone.now()  # для отображения текущего времени

    if request.method == 'POST':
        # Извлекаем данные из формы
        content = request.POST.get('comment', '').strip()
        reaction_str = request.POST.get('reaction')  # ожидается "1" или "-1"

        # Преобразуем значение реакции в целое число
        try:
            reaction_val = int(reaction_str)
        except (TypeError, ValueError):
            reaction_val = 0

        # Если значение реакции не равно 1 или -1, сбрасываем его в 0
        if reaction_val not in (1, -1):
            reaction_val = 0

        # Если одновременно переданы комментарий и лайк/дизлайк
        if content and reaction_val:
            Comment.objects.create(post=text_instance, user=request.user, content=content)
            update_like(text_instance, request.user, reaction_val)
        # Если передан только комментарий
        elif content:
            Comment.objects.create(post=text_instance, user=request.user, content=content)
        # Если передан только лайк/дизлайк
        elif reaction_val:
            update_like(text_instance, request.user, reaction_val)

        # Редирект после POST, чтобы избежать повторной отправки формы
        return redirect('articles_url', url=url)

    # Для GET-запроса получаем актуальные комментарии и вычисляем количество лайков
    comments = text_instance.comments.all()

    like_count = Like.objects.filter(post=text_instance, reaction=1).count()
    dislike_count = Like.objects.filter(post=text_instance, reaction=-1).count()
    count_like = like_count - dislike_count  # итоговая сумма лайков

    return render(request, 'article_detail.html', {
        'article': text_instance,
        'url': url,
        'comments': comments,
        'current_time': current_time,
        'like_count': count_like,
    })



def focus_list_view(request):
    url_instances = Url.objects.filter(user=request.user)
    return render(request, 'url_art.html', {'article': url_instances})

def focus_popular_view(request):
    return render(request,'focus_popular.html')


