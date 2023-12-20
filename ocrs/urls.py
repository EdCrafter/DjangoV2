from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer_portal/',include('customer_portal.urls')),
    path('chef_portal/',include('chef_portal.urls')),
    path('',include('home.urls')),
]
