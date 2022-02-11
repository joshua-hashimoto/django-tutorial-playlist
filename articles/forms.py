import re

from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    thumbnail = forms.ImageField(
        label='サムネイル',
        widget=forms.ClearableFileInput(),
        required=False
    )
    description = forms.CharField(max_length=250, widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}))

    class Meta:
        model = Article
        fields = (
            "thumbnail",
            "slug",
            "title",
            "description",
            "content",
        )
        widgets = {
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 7}),
        }

    # モデル側のバリデーションが効く
    # def clean_slug(self):
    #     slug = self.cleaned_data.get("slug", None)
    #     alnum_regex = "[0-9a-z][0-9a-zA-Z]"
    #     regex_pattern = re.compile(alnum_regex)
    #     if not regex_pattern.match(slug):
    #         raise forms.ValidationError("slugは必ず英数字で入力して下さい")
    #     return slug

    def clean_title(self):
        cleaned_data = self.cleaned_data  # dictionary
        title: str = cleaned_data.get('title')
        error_words = ["office", ]
        if title.lower().strip() in error_words:
            raise forms.ValidationError('諸事情により、このタイトルは不正です。')
        return title
