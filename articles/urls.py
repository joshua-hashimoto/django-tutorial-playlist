from django.urls import path

from .views import article_list, article_detail

app_name = "articles"


urlpatterns = [
    path("<slug:article_slug>/", article_detail, name="article_detail"),
    path("", article_list, name="article_list"),
]
