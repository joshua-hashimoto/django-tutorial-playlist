# https://docs.djangoproject.com/ja/4.0/ref/models/fields/#model-field-types

from django.db import models
from django.urls import reverse


def upload_image_to(instance, filename):
    image_path = f"article/images/{filename}"
    return image_path


class Article(models.Model):
    thumbnail = models.ImageField(upload_to=upload_image_to, blank=True, null=True)
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
