from django.shortcuts import render
from django.views.generic import ListView

from .models import Deal

class MainView(ListView):
    model = Deal
    template_name = 'base.html'
    context_object_name = 'deals'
