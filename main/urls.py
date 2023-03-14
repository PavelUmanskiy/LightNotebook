from django.urls import path

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
    path('new_task/', TaskCreate.as_view(), name='new_task'),
    path('new_team/', TeamCreate.as_view(), name='new_team'),
    path('new_customer/', CustomerCreate.as_view(), name='new_customer'),
    path('new_employee/', EmployeeCreate.as_view(), name='new_employee'),
]
