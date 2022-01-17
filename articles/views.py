from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ArticleForm
from .models import Article


def article_list_view(request):
    articles = Article.objects.all()
    context = {
        "object_list": articles,
    }
    template_name = "articles/article_list.html"
    return render(request, template_name, context)


def article_detail_view(request, article_slug):
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


def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        # form.cleaned_data -> 辞書
        article = Article.objects.create(**form.cleaned_data)
        return redirect("articles:article_detail", article_slug=article.slug)
    context = {
        "form": form,
    }
    template_name = "articles/article_create.html"
    return render(request, template_name, context)
