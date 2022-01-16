# https://docs.djangoproject.com/ja/4.0/ref/models/fields/#model-field-types

from django.db import models
from django.urls import reverse


class Article(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # TODO: サムネイルを追加する
    # TODO: 作成者を追加する
    # TODO: タグを追加する

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:article_detail", kwargs={"article_slug": self.slug})

    def get_description(self):
        description = self.description
        if len(description) > 50:
            return description[:50] + "..."
        return description
