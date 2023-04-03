from django.urls import path
from django.views.decorators.clickjacking import xframe_options_sameorigin

from .views import *


urlpatterns = [
    path('association/<int:association_id>/', MainView.as_view(), name='main'),
    path('association/<int:association_id>/group/<int:group_id>/',
         GroupView.as_view(), name='group_view'),
    path('choose/', AssociationPickView.as_view(), name='association_picker'),
    path('manager/<int:pk>/', ManagerView.as_view(), name='manager'),
    path('team/<int:pk>/', TeamView.as_view(), name='team'),
    path('customer/<int:pk>/', CustomerView.as_view(), name='customer'),
    
    
    path('new_deal/', DealCreate.as_view(), name='new_deal'),
    path('new_task/', xframe_options_sameorigin(TaskCreate.as_view()),
         name='new_task'),
    path('new_team/', xframe_options_sameorigin(TeamCreate.as_view()),
         name='new_team'),
    path('new_customer/', xframe_options_sameorigin(CustomerCreate.as_view()),
         name='new_customer'),
    path('new_employee/', xframe_options_sameorigin(EmployeeCreate.as_view()),
         name='new_employee'),
    path('new_group/', xframe_options_sameorigin(GroupCreate.as_view()),
         name='new_group'),
]
