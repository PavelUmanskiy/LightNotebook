from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Association, Manager


class MainView(LoginRequiredMixin, ListView):
    model = Association
    template_name = 'index.html'
    context_object_name = 'association'
    
    def get_queryset(self):
        # Load only manager's specific association, situation when manager
        # belongs to different associations - TODO
        self.queryset = \
            Manager.objects.get(user=self.request.user.id).association_set.all()
        return super().get_queryset()    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for association in self.queryset:
            context['deals'] = association.deals.all().order_by('-id')
            context['association_for_utils'] = association
        return context