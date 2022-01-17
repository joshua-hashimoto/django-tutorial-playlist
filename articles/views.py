from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404

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
    if request.method == "POST":
        form = request.POST
        try:
            slug = form.get("slug", None)
            title = form.get("title", None)
            description = form.get("description", None)
            content = form.get("content", None)
            # new_article = Article(slug=slug, title=title, description=description, content=content)
            # new_article.save()
            Article.objects.create(slug=slug, title=title, description=description, content=content)
        except Exception:
            raise HttpResponseBadRequest
    context = {}
    template_name = "articles/article_create.html"
    return render(request, template_name, context)
