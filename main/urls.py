from django.urls import path

from .views import *


urlpatterns = [
    path('association/<int:association_id>/', MainView.as_view(), name='main'),
    path('association/<int:association_id>/group/<int:group_id>/',
         GroupView.as_view(), name='group_view'),
    path('choose/', AssociationPickView.as_view(), name='association_picker'),
]
