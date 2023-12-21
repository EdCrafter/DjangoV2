from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from customer_portal.models import *
from django.contrib.auth.decorators import login_required
from chef_m_portal.models import *
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
    date = request.POST['date']
    try:
        user = User.objects.create_user(username = username, password = password, email = email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    except:
        return render(request, 'customer/registration_error.html')
    try:
        area = Area.objects.get(city = city, date = date)
    except:
        area = None
    if area is not None:
        customer = Customer(user = user, mobile = mobile, area = area)
    else:
        area = Area(city = city, date = date)
        area.save()
        area = Area.objects.get(city = city, date = date)
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
    tables_list = []
    area = Area.objects.filter(city = city)
    for a in area:
        tables = tables.objects.filter(area = a)
        for tableO in tables:
            if tableO.is_available == True:
                table_dictionary = {'name':tableO.table_name, 'shape':tableO.shape, 'id':tableO.id, 'date':tableO.area.date, 'seats':tableO.seats, 'size':tableO.size}
                tables_list.append(table_dictionary)
    request.session['tables_list'] = tables_list
    return render(request, 'customer/search_results.html')


@login_required
def rent_table(request):
    id = request.POST['id']
    table = tables.objects.get(id = id)
    cost_per_day = int(table.seats)*13
    return render(request, 'customer/confirmation.html', {'table':table, 'cost_per_day':cost_per_day})

@login_required
def confirm(request):
    table_id = request.POST['id']
    username = request.user
    user = User.objects.get(username = username)
    days = request.POST['days']
    table = tables.objects.get(id = table_id)
    if table.is_available:
        chef_m = table.people
        rent = (int(table.seats))*13*(int(days))
        chef_m.wallet += rent
        chef_m.save()
        try:
            order = Orders(table = table, chef_m = chef_m, user = user, rent=rent, days=days)
            order.save()
        except:
            order = Orders.objects.get(table = table, chef_m = chef_m, user = user, rent=rent, days=days)
        table.is_available = False
        table.save()
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
                order_dictionary = {'id':o.id,'rent':o.rent, 'table':o.table, 'days':o.days, 'chef_m':o.chef_m}
                order_list.append(order_dictionary)
    return render(request, 'customer/manage.html', {'od':order_list})

@login_required
def update_order(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
    table = order.table
    table.is_available = True
    table.save()
    chef_m = order.chef_m
    chef_m.wallet -= int(order.rent)
    chef_m.save()
    order.delete()
    cost_per_day = int(table.seats)*13
    return render(request, 'customer/confirmation.html', {'table':table}, {'cost_per_day':cost_per_day})

@login_required
def delete_order(request):
    order_id = request.POST['id']
    order = Orders.objects.get(id = order_id)
    chef_m = order.chef_m
    chef_m.wallet -= int(order.rent)
    chef_m.save()
    table = order.table
    table.is_available = True
    table.save()
    order.delete()
    return HttpResponseRedirect('/customer_portal/manage/')
