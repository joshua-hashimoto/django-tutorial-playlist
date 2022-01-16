from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Article


def article_list(request):
    articles = Article.objects.all()
    context = {
        "object_list": articles,
    }
    template_name = "articles/article_list.html"
    return render(request, template_name, context)


def article_detail(request, article_slug):
    # try:
    #     article = Article.objects.get(slug=article_slug)
    # except:
    #     raise Http404

    article = get_object_or_404(Article, slug=article_slug)
    context = {
        "object": article,
    }
    template_name = "articles/article_detail.html"
    return render(request, template_name, context)
