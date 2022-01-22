from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def login_view(request):
    context = {}
    template_name = "accounts/login.html"
    return render(request, template_name, context)


def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        # ユーザーの登録に成功したら、ログイン画面へ遷移する
        return redirect("accounts:login")

    context = {
        "form": form,
    }
    template_name = "accounts/signup.html"
    return render(request, template_name, context)


def logout_view(request):
    # ログアウトはモーダルを使ってやるため、基本的にはredirectしかしない
    context = {}
    template_name = "accounts/logout_modal.html"
    return redirect("articles:article_list")
