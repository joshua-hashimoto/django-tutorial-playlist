import random

from django.http import HttpResponse


def index_view(request):
    name = 'John'
    random_number = random.randint(1, 5000)

    context = {
        'name': name,
        'random_number': random_number,
    }

    HTML_STRING = """
    <h1>Hi {name}!</h1>
    <p>Today's lucky number is... {random_number}</>
    """.format(**context)
    return HttpResponse(HTML_STRING)


def about_view(request):
    return HttpResponse("About page")
