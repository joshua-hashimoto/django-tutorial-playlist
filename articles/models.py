# https://docs.djangoproject.com/ja/4.0/ref/models/fields/#model-field-types

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse


User = settings.AUTH_USER_MODEL


class ArticleQuerySet(models.QuerySet):
    def all(self):
        return self.filter(is_active=True)

    def search(self, query_string=None):
        if query_string is None:
            return self.all()
        lookup = (
            Q(is_active=True)
            & (Q(title__icontains=query_string)
               | Q(description__icontains=query_string))

        )
        return self.filter(lookup)

    def all_deleted(self):
        return self.filter(is_active=False)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all()

    def search(self, query_string=None):
        queryset = self.get_queryset().search(query_string)
        return queryset

    def all_deleted(self):
        return self.get_queryset().all_deleted()


def upload_image_to(instance, filename):
    image_path = f"article/images/{filename}"
    return image_path


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=upload_image_to, blank=True, null=True)
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # TODO: タグを追加する

    objects = ArticleManager()

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:article_detail", kwargs={"article_slug": self.slug})

    def get_description(self):
        description = self.description
        if len(description) > 50:
            return description[:50] + "..."
        return description
