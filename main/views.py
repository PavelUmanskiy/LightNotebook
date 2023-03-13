from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    Association,
    Customer,
    Manager,
    Group,
    Team,
    )
 

class MainView(LoginRequiredMixin, ListView):
    model = Association
    template_name = 'index.html'
    context_object_name = 'association'
    
    def get_queryset(self):
        self.queryset = Manager.objects.get(user=self.request.user.id)\
            .association_set.get(pk=self.kwargs['association_id'])
        return super().get_queryset()    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context.items(), self.kwargs.items(), sep='\n'+'#'*50+'\n')
        context['deals'] = self.queryset.deals.all().order_by('-id')
        context['association_for_utils'] = self.queryset
        context['group_id'] = 0
        return context

    def dispatch(self, request, *args, **kwargs):
        self.request.session['last_association'] = self.kwargs['association_id']
        return super().dispatch(request, *args, **kwargs)


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

    def dispatch(self, request, *args, **kwargs):
        self.request.session['last_association'] = self.kwargs['association_id']
        return super().dispatch(request, *args, **kwargs)


class AssociationPickView(LoginRequiredMixin, ListView):
    model = Association
    template_name = 'secondary/association_picker.html'
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


class ManagerView(LoginRequiredMixin, DetailView):
    model = Manager
    template_name = 'secondary/manager.html'
    context_object_name = 'manager'
    
    def get_queryset(self):
        self.queryset = Manager.objects.filter(pk=self.kwargs['pk'])
        return super().get_queryset()
                    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['association_for_utils'] = Association.objects\
            .get(pk=self.request.session['last_association'])
        context['teams'] = Manager.objects.get(pk=self.kwargs['pk'])\
            .team_set.only('name', 'description')
        return context
    
    
class TeamView(LoginRequiredMixin, DetailView):
    model = Team
    template_name = 'secondary/team.html'
    context_object_name = 'team'
    
    def get_queryset(self):
        self.queryset = Team.objects.filter(pk=self.kwargs['pk'])
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['association_for_utils'] = Association.objects\
            .get(pk=self.request.session['last_association'])
        return context
    

class CustomerView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'secondary/customer.html'
    context_object_name = 'customer'
    
    def get_queryset(self):
        self.queryset = Customer.objects.filter(pk=self.kwargs['pk'])
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['association_for_utils'] = Association.objects\
            .get(pk=self.request.session['last_association'])
        return context
    
    