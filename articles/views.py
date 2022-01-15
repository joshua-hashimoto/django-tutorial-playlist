from django.shortcuts import render

from .models import Article


def article_list(request):
    articles = Article.objects.all()
    context = {
        "object_list": articles,
    }
    template_name = "articles/article_list.html"
    return render(request, template_name, context)
