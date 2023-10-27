from django.shortcuts import render
from django.views.generic import ListView

from myapp.models import Task


class StartPageView(ListView):
    template_name = 'myapp/index.html'
    model = Task

