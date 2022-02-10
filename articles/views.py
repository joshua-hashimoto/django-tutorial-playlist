from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ArticleForm
from .models import Article


def article_list_view(request):
    # 1: 記事が基本的に公開日以降のものを返す <--> 現在日時より前に公開日が設定されている記事に関しては基本的に表示しない
    # 2: アクセスしているユーザーの記事は全て表示する
    articles = Article.objects.published()
    if request.user.is_authenticated:
        user_articles = Article.objects.filter(author=request.user, is_active=True)
        # (articles | user_articles)で2つのクエリセットを一緒にし、.distinct()で重複しているデータを排除
        articles = (articles | user_articles).distinct()
    if query_string := request.GET.get("query", None):
        articles = Article.objects.search(query_string)
    # articles = Article.objects.filter(is_active=False)
    # articles = Article.objects.all_deleted()
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

    article = get_object_or_404(Article, slug=article_slug, is_active=True)
    is_user_article = article.author == request.user
    context = {
        "object": article,
        "is_user_article": is_user_article,
    }
    template_name = "articles/article_detail.html"
    return render(request, template_name, context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # form.cleaned_data -> 辞書
        # article = form.save(commit=False)
        # article.title += ": ☆"
        # article.save()
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return redirect("articles:article_detail", article_slug=article.slug)
    context = {
        "form": form,
        "back_url": reverse("articles:article_list"),
    }
    template_name = "articles/article_create.html"
    return render(request, template_name, context)


@login_required
def article_edit_view(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug, author=request.user)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save()
        return redirect("articles:article_detail", article_slug=article.slug)

    context = {
        "form": form,
        "object": article,
        "back_url": reverse("articles:article_detail", kwargs={"article_slug": article.slug}),
    }
    template_name = "articles/article_edit.html"
    return render(request, template_name, context)


@login_required
def article_delete_view(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug, author=request.user)

    if request.method == "POST":
        article.is_active = False
        article.save()
        success_url = reverse("articles:article_list")
        return redirect(success_url)

    success_url = reverse("articles:article_detail", kwargs={"article_slug": article.slug})
    return redirect(success_url)
