import random

from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    name = 'John'
    random_number = random.randint(1, 5000)

    context = {
        'name': name,
        'random_number': random_number,
    }
    template_name = "index.html"
    return render(request, template_name, context)


def about_view(request):
    template_name = "about.html"
    return render(request, template_name)
