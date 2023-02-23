from django.shortcuts import render
from django.views.generic import ListView

from .models import Deal

class MainView(ListView):
    model = Deal
    template_name = 'TODO'
    context_object_name = 'deals'
