from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Notebook

def home(request):
    notebooks = Notebook.objects.all()
    notebook_titles = list()

    for notebook in notebooks:
        notebook_titles.append(notebook.title)

    response_html = '<br>'.join(notebook_titles)

    return HttpResponse(response_html)