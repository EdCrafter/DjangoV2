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
            chef_m = manager.objects.get(chef_m = user)
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
    date = request.POST['date']

    try:
        user = User.objects.create_user(username = username, password = password, email = email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    except:
        return render(request, 'chef_m/registration_error.html')

    try:
        area = Area.objects.get(city = city, date = date)
    except:
        area = None
    if area is not None:
        chef_m = manager(chef_m = user, mobile = mobile, area=area)
    else:
        area = Area(city = city, date = date)
        area.save()
        area = Area.objects.get(city = city, date = date)
        chef_m = manager(chef_m = user, mobile = mobile, area=area)
    chef_m.save()
    return render(request, 'chef_m/registered.html')

@login_required
def add_table(request):
    table_name = request.POST['table_name']
    shape = request.POST['shape']
    cd = manager.objects.get(chef_m=request.user)

    city = request.POST['city']
    city = city.lower()
    date = request.POST['date']
    size = request.POST['size']
    seats = request.POST['seats']
    try:
        area = Area.objects.get(city = city, date = date)
    except:
        area = None
    if area is not None:
        tableO = tables(table_name=table_name, shape=shape, people=cd, area = area, size = size, seats=seats)
    else:
        area = Area(city = city, date = date)
        area.save()
        area = Area.objects.get(city = city, date = date)
        tableO = tables(table_name=table_name, shape=shape, people=cd, area = area,size=size, seats=seats)
    tableO.save()
    return render(request, 'chef_m/table_added.html')


@login_required
def manage_tables(request):
    username = request.user
    user = User.objects.get(username = username)
    chef_m = manager.objects.get(chef_m = user)
    table_list = []
    tables1 = tables.objects.filter(people = chef_m)
    for v in tables1:
        table_list.append(v)
    return render(request, 'chef_m/manage.html', {'table_list':table_list})

@login_required
def order_list(request):
    username = request.user
    user = User.objects.get(username = username)
    chef_m = manager.objects.get(chef_m = user)
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
    table = order.table
    order.is_complete = True
    order.save()
    table.is_available = True
    table.save()
    return HttpResponseRedirect('/chef_m_portal/order_list/')



@login_required
def history(request):
    user = User.objects.get(username = request.user)
    chef_m = manager.objects.get(chef_m = user)
    orders = Orders.objects.filter(chef_m = chef_m)
    order_list = []
    for o in orders:
        order_list.append(o)
    return render(request, 'chef_m/history.html', {'wallet':chef_m.wallet, 'order_list':order_list})


@login_required
def delete(request):
    veh_id = request.POST['id']
    table = tables.objects.get(id = veh_id)
    table.delete()
    return HttpResponseRedirect('/chef_m_portal/manage_tables/')

