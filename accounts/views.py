from django.shortcuts import render, redirect


def login_view(request):
    context = {}
    template_name = "accounts/login.html"
    return render(request, template_name, context)


def signup_view(request):
    context = {}
    template_name = "accounts/signup.html"
    return render(request, template_name, context)


def logout_view(request):
    # ログアウトはモーダルを使ってやるため、基本的にはredirectしかしない
    context = {}
    template_name = "accounts/logout_modal.html"
    return redirect("articles:article_list")
