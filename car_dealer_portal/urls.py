from django.urls import path,include
from car_dealer_portal.views import *

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
