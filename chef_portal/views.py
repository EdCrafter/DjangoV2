from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
<<<<<<<< HEAD:chef_m_portal/views.py
from chef_m_portal.models import *
========
from chef_portal.models import *
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py
from customer_portal.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.is_authenticated:
<<<<<<<< HEAD:chef_m_portal/views.py
        return render(request, 'chef_m/login.html')
    else:
        return render(request, 'chef_m/home_page.html')

def login(request):
    return render(request, 'chef_m/login.html')
========
        return render(request, 'chef/login.html')
    else:
        return render(request, 'chef/home_page.html')

def login(request):
    return render(request, 'chef/login.html')
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py


def auth_view(request):
    if request.user.is_authenticated:
<<<<<<<< HEAD:chef_m_portal/views.py
        return render(request, 'chef_m/home_page.html')
========
        return render(request, 'chef/home_page.html')
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
<<<<<<<< HEAD:chef_m_portal/views.py
            chef_m = CarDealer.objects.get(chef_m = user)
        except:
            chef_m = None
        if chef_m is not None:
            auth.login(request, user)
            return render(request, 'chef_m/home_page.html')
        else:
            return render(request, 'chef_m/login_failed.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'chef_m/login.html')

def register(request):
    return render(request, 'chef_m/register.html')
========
            chef = CarDealer.objects.get(chef = user)
        except:
            chef = None
        if chef is not None:
            auth.login(request, user)
            return render(request, 'chef/home_page.html')
        else:
            return render(request, 'chef/login_failed.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'chef/login.html')

def register(request):
    return render(request, 'chef/register.html')
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py

def registration(request):
    username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    city = request.POST['city']
    city = city.lower()
    pincode = request.POST['date']

    try:
        user = User.objects.create_user(username = username, password = password, email = email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    except:
<<<<<<<< HEAD:chef_m_portal/views.py
        return render(request, 'chef_m/registration_error.html')
========
        return render(request, 'chef/registration_error.html')
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py
    try:
        area = Area.objects.get(city = city, pincode = pincode)
    except:
        area = None
    if area is not None:
<<<<<<<< HEAD:chef_m_portal/views.py
        chef_m = CarDealer(chef_m = user, mobile = mobile, area=area)
========
        chef = CarDealer(chef = user, mobile = mobile, area=area)
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py
    else:
        area = Area(city = city, pincode = pincode)
        area.save()
        area = Area.objects.get(city = city, pincode = pincode)
<<<<<<<< HEAD:chef_m_portal/views.py
        chef_m = CarDealer(chef_m = user, mobile = mobile, area=area)
    chef_m.save()
    return render(request, 'chef_m/registered.html')
========
        chef = CarDealer(chef = user, mobile = mobile, area=area)
    chef.save()
    return render(request, 'chef/registered.html')
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py

@login_required
def add_vehicle(request):
    table_name = request.POST['table_name']
    color = request.POST['shape']
<<<<<<<< HEAD:chef_m_portal/views.py
    cd = CarDealer.objects.get(chef_m=request.user)
========
    cd = CarDealer.objects.get(chef=request.user)
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py
    city = request.POST['city']
    city = city.lower()
    pincode = request.POST['date']
    description = request.POST['size']
    capacity = request.POST['seats']
    try:
        area = Area.objects.get(city = city, pincode = pincode)
    except:
        area = None
    if area is not None:
        car = Vehicles(table_name=table_name, color=color, dealer=cd, area = area, description = description, capacity=capacity)
    else:
        area = Area(city = city, pincode = pincode)
        area.save()
        area = Area.objects.get(city = city, pincode = pincode)
        car = Vehicles(table_name=table_name, color=color, dealer=cd, area = area,description=description, capacity=capacity)
    car.save()
<<<<<<<< HEAD:chef_m_portal/views.py
    return render(request, 'chef_m/vehicle_added.html')
========
    return render(request, 'chef/vehicle_added.html')
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py

@login_required
def manage_vehicles(request):
    username = request.user
    user = User.objects.get(username = username)
<<<<<<<< HEAD:chef_m_portal/views.py
    chef_m = CarDealer.objects.get(chef_m = user)
    vehicle_list = []
    vehicles = Vehicles.objects.filter(dealer = chef_m)
    for v in vehicles:
        vehicle_list.append(v)
    return render(request, 'chef_m/manage.html', {'vehicle_list':vehicle_list})
========
    chef = CarDealer.objects.get(chef = user)
    vehicle_list = []
    vehicles = Vehicles.objects.filter(dealer = chef)
    for v in vehicles:
        vehicle_list.append(v)
    return render(request, 'chef/manage.html', {'vehicle_list':vehicle_list})
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py

@login_required
def order_list(request):
    username = request.user
    user = User.objects.get(username = username)
<<<<<<<< HEAD:chef_m_portal/views.py
    chef_m = CarDealer.objects.get(chef_m = user)
    orders = Orders.objects.filter(chef_m = chef_m)
========
    chef = CarDealer.objects.get(chef = user)
    orders = Orders.objects.filter(chef = chef)
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py
    order_list = []
    for o in orders:
        if o.is_complete == False:
            order_list.append(o)
<<<<<<<< HEAD:chef_m_portal/views.py
    return render(request, 'chef_m/order_list.html', {'order_list':order_list})
========
    return render(request, 'chef/order_list.html', {'order_list':order_list})
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py

@login_required
def complete(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
    vehicle = order.vehicle
    order.is_complete = True
    order.save()
    vehicle.is_available = True
    vehicle.save()
<<<<<<<< HEAD:chef_m_portal/views.py
    return HttpResponseRedirect('/chef_m_portal/order_list/')
========
    return HttpResponseRedirect('/chef_portal/order_list/')
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py


@login_required
def history(request):
    user = User.objects.get(username = request.user)
<<<<<<<< HEAD:chef_m_portal/views.py
    chef_m = CarDealer.objects.get(chef_m = user)
    orders = Orders.objects.filter(chef_m = chef_m)
    order_list = []
    for o in orders:
        order_list.append(o)
    return render(request, 'chef_m/history.html', {'wallet':chef_m.wallet, 'order_list':order_list})
========
    chef = CarDealer.objects.get(chef = user)
    orders = Orders.objects.filter(chef = chef)
    order_list = []
    for o in orders:
        order_list.append(o)
    return render(request, 'chef/history.html', {'wallet':chef.wallet, 'order_list':order_list})
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py

@login_required
def delete(request):
    veh_id = request.POST['id']
    vehicle = Vehicles.objects.get(id = veh_id)
    vehicle.delete()
<<<<<<<< HEAD:chef_m_portal/views.py
    return HttpResponseRedirect('/chef_m_portal/manage_vehicles/')
========
    return HttpResponseRedirect('/chef_portal/manage_vehicles/')
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/views.py
