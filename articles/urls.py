from django.urls import path

from .views import article_list

app_name = "articles"


urlpatterns = [
    path("", article_list, name="article_list"),
]
