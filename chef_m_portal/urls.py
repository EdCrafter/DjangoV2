from django.urls import path,include

from chef_m_portal.views import *


urlpatterns = [
    path('index/',index),
    path('login/',login),
    path('auth/',auth_view),
    path('logout/',logout_view),
    path('register/',register),
    path('registration/',registration),
    path('add_table/',add_table),
    path('manage_tables/',manage_tables),
    path('order_list/',order_list),
    path('complete/',complete),
    path('history/',history),
    path('delete/',delete),
]
