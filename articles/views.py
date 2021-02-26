from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect

from .models import Article


def index(request):
    template = loader.get_template('articles/index.html')
    articles_list = Article.objects.all()
    context = {
        'articles_list': articles_list,
    }
    return HttpResponse(template.render(context, request))


def create_article_form(request):
    return render(request, 'articles/create_article.html')


def edit_article_form(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article_pk': article.pk,
        'article_title': article.title,
        'content_snippet': article.content_snippet
    }
    return render(request, 'articles/edit_article.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article})


def save_article(request):
    if request.method == 'POST':
        article_title = request.POST.get('article_title')
        content_snippet = request.POST.get('content_snippet')
        article = Article(title=article_title, content_snippet=content_snippet)
        article.save()
        return redirect('index')


def update_article(request):
    if request.method == 'POST':
        article_pk = request.POST.get('article_pk')
        article_title = request.POST.get('article_title')
        content_snippet = request.POST.get('content_snippet')
        article = Article.objects.get(pk=article_pk)
        article.title = article_title
        article.content_snippet = content_snippet
        article.save()
        return redirect('index')


def delete_article(request, article_id):
    Article.objects.get(pk=article_id).delete()
    return redirect('index')
