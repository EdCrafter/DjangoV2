from django.urls import path,include
<<<<<<<< HEAD:chef_m_portal/urls.py
from chef_m_portal.views import *
========
from chef_portal.views import *
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/urls.py

urlpatterns = [
    path('index/',index),
    path('login/',login),
    path('auth/',auth_view),
    path('logout/',logout_view),
    path('register/',register),
    path('registration/',registration),
    path('add_vehicle/',add_vehicle),
    path('manage_vehicles/',manage_vehicles),
    path('order_list/',order_list),
    path('complete/',complete),
    path('history/',history),
    path('delete/',delete),
]
