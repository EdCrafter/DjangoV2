from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer_portal/',include('customer_portal.urls')),
<<<<<<< HEAD
    path('chef_m_portal/',include('chef_m_portal.urls')),
=======
    path('chef_portal/',include('chef_portal.urls')),
>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba
    path('',include('home.urls')),
]
