from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from  django.contrib.auth.models import User,auth
from .models import Country, State, City, Area, Property, Users
from django.http import HttpResponse, JsonResponse

import random
import string

from django.contrib.auth import login,authenticate
from django.conf import settings
# Create your views here.
def index(request):

    return render(request,"dashboard.html")

def helo(request):
    return  HttpResponse('<h1> Hello world </h1>')

def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print('email',email)

        user=auth.authenticate(email=email,password=password)
        return redirect('/')

    return render(request, 'sign-in.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print('username')
        user = User.objects.create_user(username=username,email=email, password=password)
        user.save()
        subject = 'verification mail'
        message = 'Thanks for creating an account from outliers'
        recepient = [email]
        try:
            send_mail(subject, message, 'Sandhya.vishnu.08.28@gmail.com', ['hema.v181@gmail.com'],fail_silently=False)
        except Exception as e:
            print(e)
        return render(request, 'success.html')

    else:
        return render(request, 'sign-up.html')

def country_view(request):
    country_id = request.GET.get('id')
    country_one = []
    if country_id:
        country_one = Country.objects.get(id=country_id)
    country = Country.objects.filter(deleted=False).order_by('country')
    if country_one.status == True:
        country_one.status = "Active"
    else:
        country_one.status = "Inactive"
    return render(request, "country/country_view.html",
                  {'country': country, 'country_one': country_one})

def country_list(request):
    country_id = request.GET.get('id')
    country_one = []
    if country_id:
        country_one = Country.objects.get(id=country_id)
    country = Country.objects.filter(deleted=False).order_by('country')
    for countries in country:
        if countries.status == True:
            countries.status = "Active"
        else:
            countries.status = "Inactive"
    return render(request, "country/country_list.html",
                  {'country': country, 'country_one': country_one})

def country_add(request):
    country_id = request.GET.get('id')
    country_qs = []
    if country_id:
        country_qs = Country.objects.get(id=int(country_id), deleted=False)
    return render(request, 'country/country_add.html', {'country_qs': country_qs})

def country_edit(request):
    country_id = request.POST.get('country_id')
    country = request.POST.get('country')
    status = request.POST.get('status')
    if country_id:
        country_qs = Country.objects.get(id=int(country_id), deleted=False)
        country_qs.country = country
        country_qs.status = status
        country_qs.save()
    else:
        country = Country(country=country, status=status)
        country.save()
    return redirect("aragonapp:country_list")

def country_delete(request):
    country_id = request.GET.get('id')
    if country_id:
        country = Country.objects.get(id=country_id)
        country.deleted = True
        country.save()
        return redirect("aragonapp:country_list")

# STATE FUNCTIONS STARTS
def state_list(request):
    state_id = request.GET.get('id')
    state_one = []

    if state_id:
        state_one = State.objects.get(id=state_id, deleted=False)
    state = State.objects.filter(deleted=False).order_by('state')
    for states in state:
        if states.status == True:
            states.status = "Active"
        else:
            states.status = "Inactive"
    return render(request, "state/state_list.html",
                  {'state': state, 'state_one': state_one})

def state_view(request):
    state_id = request.GET.get('id')
    state_one = []

    if state_id:
        state_one = State.objects.get(id=state_id, deleted=False)
    state = State.objects.filter(deleted=False).order_by('state')
    if state_one.status == True:
        state_one.status = "Active"
    else:
        state_one.status = "Inactive"
    return render(request, "state/state_view.html",
                  {'state': state, 'state_one': state_one})

def state_add(request):
    state_id = request.GET.get('id')
    state_qs = []
    if state_id:
        state_qs = State.objects.get(id=int(state_id), deleted=False)
    countries = Country.objects.filter(deleted=False).order_by('country')
    return render(request, 'state/state_add.html', {'state_qs': state_qs, 'countries': countries})

def state_edit(request):
    state_id = request.POST.get('state_id')
    country = request.POST.get('country')
    state = request.POST.get('state')
    status = request.POST.get('status')
    country_one = Country.objects.get(id=country, deleted=False)
    if state_id:
        state_qs = State.objects.get(id=int(state_id), deleted=False)
        state_qs.country = country_one
        state_qs.state = state
        state_qs.status = status
        state_qs.save()
    else:
        state = State(country=country_one, state=state, status=status)
        state.save()
    return redirect("aragonapp:state_list")

def state_delete(request):
    state_id = request.GET.get('id')
    if state_id:
        state = State.objects.get(id=state_id)
        state.deleted = True
        state.save()
        return redirect("aragonapp:state_list")

def city_list(request):
    city_id = request.GET.get('id')
    city_one = []
    if city_id:
        city_one = City.objects.get(id=city_id, deleted=False)
    city = City.objects.filter(deleted=False).order_by('city')
    for cities in city:
        if cities.status == True:
            cities.status = "Active"
        else:
            cities.status = "Inactive"
    return render(request, "city/city_list.html",
                  {'city': city, 'city_one': city_one})

def city_view(request):
    city_id = request.GET.get('id')
    city_one = []
    if city_id:
        city_one = City.objects.get(id=city_id, deleted=False)
    city = City.objects.filter(deleted=False).order_by('city')
    if city_one.status == True:
        city_one.status = "Active"
    else:
        city_one.status = "Inactive"
    return render(request, "city/city_view.html",
                  {'city': city, 'city_one': city_one})

def city_add(request):
    city_id = request.GET.get('id')
    city_qs = []
    if city_id:
        city_qs = City.objects.get(id=int(city_id), deleted=False)
    countries = Country.objects.filter(deleted=False).order_by('country')
    states = State.objects.filter(deleted=False).order_by('state')
    return render(request, 'city/city_add.html', {'city_qs': city_qs, 'countries': countries, 'states': states})

def city_edit(request):
    city_id = request.POST.get('city_id')
    country = request.POST.get('country')
    state = request.POST.get('state')
    city = request.POST.get('city')
    status = request.POST.get('status')
    country_one = Country.objects.get(id=country, deleted=False)
    state_one = State.objects.get(id=state, deleted=False)
    if city_id:
        city_qs = City.objects.get(id=int(city_id), deleted=False)
        city_qs.country = country_one
        city_qs.state = state_one
        city_qs.city = city
        city_qs.status = status
        city_qs.city = city
        city_qs.save()
    else:
        city = City(country=country_one, state=state_one, city=city, status=status)
        city.save()
    return redirect("aragonapp:city_list")

def city_delete(request):
    city_id = request.GET.get('id')
    if city_id:
        city = City.objects.get(id=city_id)
        city.deleted = True
        city.save()
        return redirect("aragonapp:city_list")

def area_list(request):
    area_id = request.GET.get('id')
    area_one = []
    if area_id:
        area_one = Area.objects.get(id=area_id, deleted=False)
    area = Area.objects.filter(deleted=False).order_by('city')
    for areas in area:
        if areas.status == True:
            areas.status = "Active"
        else:
            areas.status = "Inactive"
    return render(request, "area/area_list.html",
                  {'area': area, 'area_one': area_one})

def area_view(request):
    area_id = request.GET.get('id')
    area_one = []
    if area_id:
        area_one = Area.objects.get(id=area_id, deleted=False)
    area = Area.objects.filter(deleted=False).order_by('city')
    for areas in area:
        if areas.status == True:
            areas.status = "Active"
        else:
            areas.status = "Inactive"
    return render(request, "area/area_view.html",
                  {'area': area, 'area_one': area_one})

def area_add(request):
    area_id = request.GET.get('id')
    area_qs = []
    if area_id:
        area_qs = Area.objects.get(id=int(area_id), deleted=False)
    countries = Country.objects.filter(deleted=False).order_by('country')
    states = State.objects.filter(deleted=False).order_by('state')
    cities = City.objects.filter(deleted=False).order_by('city')
    return render(request, 'area/area_add.html', {'area_qs': area_qs, 'countries': countries, 'states': states, 'cities':cities})

def area_edit(request):
    area_id = request.POST.get('area_id')
    country = request.POST.get('country')
    state = request.POST.get('state')
    city = request.POST.get('city')
    area = request.POST.get('area')
    zipcode = request.POST.get('zipcode')
    status = request.POST.get('status')
    country_one = Country.objects.get(id=country, deleted=False)
    state_one = State.objects.get(id=state, deleted=False)
    city_one = City.objects.get(id=city, deleted=False)

    if area_id:
        area_qs = Area.objects.get(id=int(area_id), deleted=False)
        area_qs.country.country = country_one
        area_qs.state = state_one
        area_qs.city = city_one
        area_qs.area = area
        area_qs.zipcode = zipcode
        area_qs.status = status
        area_qs.save()
    else:
        area = Area(country=country_one, state=state_one, area=area, city=city_one, status=status, zipcode=zipcode)
        area.save()
    return redirect("aragonapp:area_list")

def area_delete(request):
    area_id = request.GET.get('id')
    if area_id:
        area = Area.objects.get(id=area_id)
        area.deleted = True
        area.save()
        return redirect("aragonapp:area_list")


# Property
def property_view(request):
    area_id = request.GET.get('id')
    area_one = []
    if area_id:
        area_one = Area.objects.get(id=area_id, deleted=False)
    area = Area.objects.filter(deleted=False).order_by('city')
    for areas in area:
        if areas.status == True:
            areas.status = "Active"
        else:
            areas.status = "Inactive"
    return render(request, "area/area_view.html",
                  {'area': area, 'area_one': area_one})
def property_list(request):
    template = 'property/property_list.html'
    country = Country.objects.filter(deleted=False).order_by('country')
    for countries in country:
        if countries.status == True:
            countries.status = "Active"
        else:
            countries.status = "Inactive"
    context = {'country': country}
    return render(request, template, context)

def property_add(request):
    template = 'property/property_add.html'
    context = {}
    print(request.method)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        short_description = request.POST.get('short_description')
        description = request.POST.get('description')
        built_up_area_price = request.POST.get('built_up_area_price')
        property_type = request.POST.get('property_type')
        property_for = request.POST.get('property_for')
        property_added_by_user_type = request.POST.get('property_added_by_user_type')
        property_user_id_added = request.POST.get('property_user_id_added')
        lat = request.POST.get('lat')
        long = request.POST.get('longtude')
        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        sub_area = request.POST.get('sub_area')
        size = request.POST.get('size')
        built_up_area_size = request.POST.get('built_up_area_size')
        bed_rooms = request.POST.get('bed_rooms')
        bath_rooms = request.POST.get('bath_rooms')
        parking_slots = request.POST.get('parking_slots')
        indoor_amenities = request.POST.get('indoor_amenities')
        outdoor_amenities = request.POST.get('outdoor_amenities')
        deleted = False
        status = "Active"
        import datetime;

        created_at = datetime.datetime.now()

        unique_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(128))
        # print('name', name, "short_description", short_description, "description", description, "price", price,
        #       "built_up_area_price", built_up_area_price, "property_type", property_type, "property_for", property_for,
        #       "property_added_by_user_type", property_added_by_user_type, "property_user_id_added",
        #       property_user_id_added, "lat", lat, "long", long, "address", address, "country", country, "state", state,
        #       "city", city, "zipcode", zipcode, "sub_area", sub_area, "size", size, "built_up_area_size",
        #       built_up_area_size, "bed_rooms", bed_rooms, "bath_rooms", bath_rooms, "parking_slots", parking_slots,
        #       "status", status, "unique_id", unique_id, "indoor_amenities", indoor_amenities, "outdoor_amenities",
        #       outdoor_amenities, "deleted", deleted, "created_at", created_at, "updated_at", created_at)

        property = Property(name=name,short_description=short_description,description=description,price=price,built_up_area_price=built_up_area_price,property_type=property_type,property_for=property_for,property_added_by_user_type=property_added_by_user_type,property_user_id_added=	property_user_id_added,lat=lat,long=long,address=address,country=country,state=state,city=city,zipcode=zipcode,sub_area=sub_area,size=size,	built_up_area_size=	built_up_area_size,bed_rooms=bed_rooms,bath_rooms=bath_rooms,parking_slots=parking_slots,status=status,unique_id=unique_id,indoor_amenities=indoor_amenities,outdoor_amenities=outdoor_amenities,deleted=deleted,created_at=created_at,updated_at=created_at)
        property.save()
        return redirect("aragonapp:property_list")

    return render(request,template ,context)

def property_edit(request):
    template = 'property/area_add.html'
    context = {}
    country_id = request.POST.get('country_id')
    country = request.POST.get('country')
    status = request.POST.get('status')
    if country_id:
        country_qs = Country.objects.get(id=int(country_id), deleted=False)
        country_qs.country = country
        country_qs.status = status
        country_qs.save()
    else:
        country = Country(country=country, status=status)
        country.save()
    return redirect("aragonapp:country_list")

def property_delete(request):
    template = 'property/area_add.html'
    context = {}
    country_id = request.GET.get('id')
    if country_id:
        country = Country.objects.get(id=country_id)
        country.deleted = True
        country.save()
        return redirect("aragonapp:country_list")


#Users

def users_view(request):
    area_id = request.GET.get('id')
    area_one = []
    if area_id:
        area_one = Area.objects.get(id=area_id, deleted=False)
    area = Area.objects.filter(deleted=False).order_by('city')
    for areas in area:
        if areas.status == True:
            areas.status = "Active"
        else:
            areas.status = "Inactive"
    return render(request, "area/area_view.html",
                  {'area': area, 'area_one': area_one})
def users_list(request):
    template = 'users/user_list.html'
    country = Country.objects.filter(deleted=False).order_by('country')
    for countries in country:
        if countries.status == True:
            countries.status = "Active"
        else:
            countries.status = "Inactive"
    context = {'country': country}
    return render(request, template, context)

def users_add(request):
    template = 'users/user_add.html'
    context = {}
    country_id = request.GET.get('id')
    country_qs = []
    if country_id:
        country_qs = Country.objects.get(id=int(country_id), deleted=False)
    return render(request, 'country/country_add.html', {'country_qs': country_qs})

def users_edit(request):
    template = 'users/user_add.html'
    context = {}
    country_id = request.POST.get('country_id')
    country = request.POST.get('country')
    status = request.POST.get('status')
    if country_id:
        country_qs = Country.objects.get(id=int(country_id), deleted=False)
        country_qs.country = country
        country_qs.status = status
        country_qs.save()
    else:
        country = Country(country=country, status=status)
        country.save()
    return redirect("aragonapp:country_list")

def users_delete(request):
    template = 'users/user_add.html'
    context = {}
    country_id = request.GET.get('id')
    if country_id:
        country = Country.objects.get(id=country_id)
        country.deleted = True
        country.save()
        return redirect("aragonapp:country_list")