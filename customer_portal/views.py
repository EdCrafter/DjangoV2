from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from customer_portal.models import *
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from chef_m_portal.models import *
=======
from chef_portal.models import *
>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'customer/login.html')
    else:
        return render(request, 'customer/home_page.html')

def login(request):
    return render(request, 'customer/login.html')

def auth_view(request):
    if request.user.is_authenticated:
        return render(request, 'customer/home_page.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            customer = Customer.objects.get(user = user)
        except:
            customer = None
        if customer is not None:
            auth.login(request, user)
            return render(request, 'customer/home_page.html')
        else:
            return render(request, 'customer/login_failed.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'customer/login.html')

def register(request):
    return render(request, 'customer/register.html')

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
        return render(request, 'customer/registration_error.html')
    try:
        area = Area.objects.get(city = city, pincode = pincode)
    except:
        area = None
    if area is not None:
        customer = Customer(user = user, mobile = mobile, area = area)
    else:
        area = Area(city = city, pincode = pincode)
        area.save()
        area = Area.objects.get(city = city, pincode = pincode)
        customer = Customer(user = user, mobile = mobile, area = area)

    customer.save()
    return render(request, 'customer/registered.html')

@login_required
def search(request):
    return render(request, 'customer/search.html')

@login_required
def search_results(request):
    city = request.POST['city']
    city = city.lower()
    vehicles_list = []
    area = Area.objects.filter(city = city)
    for a in area:
        vehicles = Vehicles.objects.filter(area = a)
        for car in vehicles:
            if car.is_available == True:
                vehicle_dictionary = {'name':car.table_name, 'shape':car.color, 'id':car.id, 'date':car.area.pincode, 'seats':car.capacity, 'size':car.description}
                vehicles_list.append(vehicle_dictionary)
    request.session['vehicles_list'] = vehicles_list
    return render(request, 'customer/search_results.html')


@login_required
def rent_vehicle(request):
    id = request.POST['id']
    vehicle = Vehicles.objects.get(id = id)
    cost_per_day = int(vehicle.capacity)*13
    return render(request, 'customer/confirmation.html', {'vehicle':vehicle, 'cost_per_day':cost_per_day})

@login_required
def confirm(request):
    vehicle_id = request.POST['id']
    username = request.user
    user = User.objects.get(username = username)
    days = request.POST['days']
    vehicle = Vehicles.objects.get(id = vehicle_id)
    if vehicle.is_available:
<<<<<<< HEAD
        chef_m = vehicle.dealer
        rent = (int(vehicle.capacity))*13*(int(days))
        chef_m.wallet += rent
        chef_m.save()
        try:
            order = Orders(vehicle = vehicle, chef_m = chef_m, user = user, rent=rent, days=days)
            order.save()
        except:
            order = Orders.objects.get(vehicle = vehicle, chef_m = chef_m, user = user, rent=rent, days=days)
=======
        chef = vehicle.dealer
        rent = (int(vehicle.capacity))*13*(int(days))
        chef.wallet += rent
        chef.save()
        try:
            order = Orders(vehicle = vehicle, chef = chef, user = user, rent=rent, days=days)
            order.save()
        except:
            order = Orders.objects.get(vehicle = vehicle, chef = chef, user = user, rent=rent, days=days)
>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba
        vehicle.is_available = False
        vehicle.save()
        return render(request, 'customer/confirmed.html', {'order':order})
    else:
        return render(request, 'customer/order_failed.html')

@login_required
def manage(request):
    order_list = []
    user = User.objects.get(username = request.user)
    try:
        orders = Orders.objects.filter(user = user)
    except:
        orders = None
    if orders is not None:
        for o in orders:
            if o.is_complete == False:
<<<<<<< HEAD
                order_dictionary = {'id':o.id,'rent':o.rent, 'vehicle':o.vehicle, 'days':o.days, 'chef_m':o.chef_m}
=======
                order_dictionary = {'id':o.id,'rent':o.rent, 'vehicle':o.vehicle, 'days':o.days, 'chef':o.chef}
>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba
                order_list.append(order_dictionary)
    return render(request, 'customer/manage.html', {'od':order_list})

@login_required
def update_order(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
    vehicle = order.vehicle
    vehicle.is_available = True
    vehicle.save()
<<<<<<< HEAD
    chef_m = order.chef_m
    chef_m.wallet -= int(order.rent)
    chef_m.save()
=======
    chef = order.chef
    chef.wallet -= int(order.rent)
    chef.save()
>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba
    order.delete()
    cost_per_day = int(vehicle.capacity)*13
    return render(request, 'customer/confirmation.html', {'vehicle':vehicle}, {'cost_per_day':cost_per_day})

@login_required
def delete_order(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
<<<<<<< HEAD
    chef_m = order.chef_m
    chef_m.wallet -= int(order.rent)
    chef_m.save()
=======
    chef = order.chef
    chef.wallet -= int(order.rent)
    chef.save()
>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba
    vehicle = order.vehicle
    vehicle.is_available = True
    vehicle.save()
    order.delete()
    return HttpResponseRedirect('/customer_portal/manage/')
