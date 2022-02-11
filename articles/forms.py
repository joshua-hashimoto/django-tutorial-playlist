import re

from django import forms


class ArticleForm(forms.Form):
    slug = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(max_length=250, widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    def clean_slug(self):
        slug = self.cleaned_data.get("slug", None)
        alnum_regex = "[0-9a-z][0-9a-zA-Z]"
        regex_pattern = re.compile(alnum_regex)
        if not regex_pattern.match(slug):
            raise forms.ValidationError("slugは必ず英数字で入力して下さい")
        return slug
