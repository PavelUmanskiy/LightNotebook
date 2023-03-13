from django.urls import path

from .views import *


urlpatterns = [
    path('association/<int:association_id>/', MainView.as_view(), name='main'),
    path('association/<int:association_id>/group/<int:group_id>/',
         GroupView.as_view(), name='group_view'),
    path('choose/', AssociationPickView.as_view(), name='association_picker'),
    path('manager/<int:pk>/', ManagerView.as_view(), name='manager'),
    path('team/<int:pk>/', TeamView.as_view(), name='team'),
    path('customer/<int:pk>/', CustomerView.as_view(), name='customer')
]
