from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Association, Manager, Group


class AssociationPickView(LoginRequiredMixin, ListView):
    model = Association
    template_name = 'association_picker.html'
    context_object_name = 'associations'
    
    def get_queryset(self):
        self.queryset = Manager.objects\
            .get(user=self.request.user.id).association_set.only(
                'id',
                'title',
                'description')
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['association_for_utils'] = {'id': 0}
        return context
    


class MainView(LoginRequiredMixin, ListView):
    model = Association
    template_name = 'index.html'
    context_object_name = 'association'
    
    def get_queryset(self):
        # Load only manager's specific association, situation when manager
        # belongs to different associations - TODO
        self.queryset = \
            Manager.objects.get(user=self.request.user.id).association_set.all()
        if len(self.queryset) > 1:
            return redirect('association_picker', permanent=True)
        return super().get_queryset()    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context.items(), self.kwargs.items(), sep='\n'+'#'*50+'\n')
        for association in self.queryset:
            context['deals'] = association.deals.all().order_by('-id')
            context['association_for_utils'] = association
        context['group_id'] = 0
        return context


class GroupView(LoginRequiredMixin, ListView):
    model = Association
    template_name = 'index.html'
    context_object_name = 'association'
    
    def get_queryset(self):
        self.queryset = \
            Manager.objects.get(user=self.request.user.id)\
            .association_set.prefetch_related('deals')\
            .filter(deals__deal_groups__id=self.kwargs['group_id'])
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context.items(), self.kwargs.items(), sep='\n'+'#'*50+'\n')
        for association in self.queryset:
            context['deals'] = association.deals\
                .filter(deal_groups__id=self.kwargs['group_id']).order_by('-id')
            context['association_for_utils'] = association
        context['group_name'] = \
            Group.objects.get(pk=self.kwargs['group_id']).name
        return context