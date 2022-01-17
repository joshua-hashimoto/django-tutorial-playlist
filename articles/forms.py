import re

from django import forms


class ArticleForm(forms.Form):
    slug = forms.CharField(max_length=150)
    title = forms.CharField(max_length=120)
    description = forms.CharField(max_length=250)
    content = forms.CharField(widget=forms.Textarea())

    def clean_slug(self):
        slug = self.cleaned_data.get("slug", None)
        alnum_regex = "[0-9a-z][0-9a-zA-Z]"
        regex_pattern = re.compile(alnum_regex)
        if not regex_pattern.match(slug):
            raise forms.ValidationError("slugは必ず英数字で入力して下さい")
        return slug
