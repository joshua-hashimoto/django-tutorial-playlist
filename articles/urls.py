from django.urls import path

from .views import article_list_view, article_detail_view, article_create_view, article_edit_view

app_name = "articles"


urlpatterns = [
    path("create/", article_create_view, name="article_create"),
    path("<slug:article_slug>/edit/", article_edit_view, name="article_edit"),
    path("<slug:article_slug>/", article_detail_view, name="article_detail"),
    path("", article_list_view, name="article_list"),
]
