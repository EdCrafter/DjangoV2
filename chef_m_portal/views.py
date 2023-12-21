from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

from chef_m_portal.models import *

from customer_portal.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'chef_m/login.html')
    else:
        return render(request, 'chef_m/home_page.html')

def login(request):
    return render(request, 'chef_m/login.html')



def auth_view(request):
    if request.user.is_authenticated:
        return render(request, 'chef_m/home_page.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
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
        return render(request, 'chef_m/registration_error.html')

    try:
        area = Area.objects.get(city = city, pincode = pincode)
    except:
        area = None
    if area is not None:
        chef_m = CarDealer(chef_m = user, mobile = mobile, area=area)
    else:
        area = Area(city = city, pincode = pincode)
        area.save()
        area = Area.objects.get(city = city, pincode = pincode)
        chef_m = CarDealer(chef_m = user, mobile = mobile, area=area)
    chef_m.save()
    return render(request, 'chef_m/registered.html')

@login_required
def add_vehicle(request):
    table_name = request.POST['table_name']
    color = request.POST['shape']
    cd = CarDealer.objects.get(chef_m=request.user)

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
    return render(request, 'chef_m/vehicle_added.html')


@login_required
def manage_vehicles(request):
    username = request.user
    user = User.objects.get(username = username)
    chef_m = CarDealer.objects.get(chef_m = user)
    vehicle_list = []
    vehicles = Vehicles.objects.filter(dealer = chef_m)
    for v in vehicles:
        vehicle_list.append(v)
    return render(request, 'chef_m/manage.html', {'vehicle_list':vehicle_list})

@login_required
def order_list(request):
    username = request.user
    user = User.objects.get(username = username)
    chef_m = CarDealer.objects.get(chef_m = user)
    orders = Orders.objects.filter(chef_m = chef_m)

    order_list = []
    for o in orders:
        if o.is_complete == False:
            order_list.append(o)

    return render(request, 'chef_m/order_list.html', {'order_list':order_list})


@login_required
def complete(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
    vehicle = order.vehicle
    order.is_complete = True
    order.save()
    vehicle.is_available = True
    vehicle.save()
    return HttpResponseRedirect('/chef_m_portal/order_list/')



@login_required
def history(request):
    user = User.objects.get(username = request.user)
    chef_m = CarDealer.objects.get(chef_m = user)
    orders = Orders.objects.filter(chef_m = chef_m)
    order_list = []
    for o in orders:
        order_list.append(o)
    return render(request, 'chef_m/history.html', {'wallet':chef_m.wallet, 'order_list':order_list})


@login_required
def delete(request):
    veh_id = request.POST['id']
    vehicle = Vehicles.objects.get(id = veh_id)
    vehicle.delete()
    return HttpResponseRedirect('/chef_m_portal/manage_vehicles/')

