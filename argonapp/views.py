from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from  django.contrib.auth.models import User,auth

from .models import Country, State, City, Area, Property, Users

from .models import Country, State, City, Area, Amenities, Nearby_Landmark, Package
from .models import Country, State, City, Area, Property_types, Property_for

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
=======
def amenities_list(request):
    amenities_id = request.GET.get('id')
    amenities_one = []
    if amenities_id:
        amenities_one = Amenities.objects.get(id=amenities_id, deleted=False)
    amenitie = Amenities.objects.filter(deleted=False).order_by('name')
    for amenities in amenitie:
        if amenities.status == True:
            amenities.status = "Active"
        else:
            amenities.status = "Inactive"
    return render(request, "amenities/amenities_list.html",
                  {'amenities': amenitie, 'amenities_one': amenities_one})

def amenities_view(request):
    amenities_id = request.GET.get('id')
    amenities_one = []
    if amenities_id:
        amenities_one = Amenities.objects.get(id=amenities_id, deleted=False)
    amenitie = Amenities.objects.filter(deleted=False).order_by('name')
    for amenities in amenitie:
        if amenities.status == True:
            amenities.status = "Active"
        else:
            amenities.status = "Inactive"
    return render(request, "amenities/amenities_view.html",
                  {'amenities': amenitie, 'amenities_one': amenities_one})

def amenities_add(request):
    amenities_id = request.GET.get('id')
    amenities_qs = []
    if amenities_id:
        amenities_qs = Amenities.objects.get(id=int(amenities_id), deleted=False)
    return render(request, 'amenities/amenities_add.html', {'amenities_qs': amenities_qs})

def amenities_edit(request):
    amenities_id = request.POST.get('amenities_id')
    name = request.POST.get('name')
    type = request.POST.get('type')
    status = request.POST.get('status')

    if amenities_id:
        amenities_qs = Amenities.objects.get(id=int(amenities_id), deleted=False)
        amenities_qs.name = name
        amenities_qs.type = type
        amenities_qs.status = status
        amenities_qs.save()
    else:
        amenities = Amenities(name=name, type=type, status=status)
        amenities.save()
    return redirect("aragonapp:amenities_list")

def amenities_delete(request):
    amenities_id = request.GET.get('id')
    if amenities_id:
        amenities = Amenities.objects.get(id=amenities_id)
        amenities.deleted = True
        amenities.save()
        return redirect("aragonapp:amenities_list")


def nearby_landmark_list(request):
    nearby_landmark_id = request.GET.get('id')
    nearby_landmark_one = []
    if nearby_landmark_id:
        nearby_landmark_one = Nearby_Landmark.objects.get(id=nearby_landmark_id, deleted=False)
    nearby_landmarks = Nearby_Landmark.objects.filter(deleted=False).order_by('name')
    for nearby_landmark in nearby_landmarks:
        if nearby_landmark.status == True:
            nearby_landmark.status = "Active"
        else:
            nearby_landmark.status = "Inactive"
    return render(request, "nearby_landmark/nearby_landmark_list.html",
                  {'nearby_landmarks': nearby_landmarks, 'nearby_landmark_one': nearby_landmark_one})

def nearby_landmark_view(request):
    nearby_landmark_id = request.GET.get('id')
    nearby_landmark_one = []
    if nearby_landmark_id:
        nearby_landmark_one = Nearby_Landmark.objects.get(id=nearby_landmark_id, deleted=False)
    nearby_landmarks = Nearby_Landmark.objects.filter(deleted=False).order_by('name')
    for nearby_landmark in nearby_landmarks:
        if nearby_landmark.status == True:
            nearby_landmark.status = "Active"
        else:
            nearby_landmark.status = "Inactive"
    return render(request, "nearby_landmark/nearby_landmark_view.html",
                  {'nearby_landmarks': nearby_landmarks, 'nearby_landmark_one': nearby_landmark_one})

def nearby_landmark_add(request):
    nearby_landmark_id = request.GET.get('id')
    nearby_landmark_qs = []
    if nearby_landmark_id:
        nearby_landmark_qs = Nearby_Landmark.objects.get(id=int(nearby_landmark_id), deleted=False)
    return render(request, 'nearby_landmark/nearby_landmark_add.html', {'nearby_landmark_qs': nearby_landmark_qs})

def nearby_landmark_edit(request):
    nearby_landmark_id = request.POST.get('nearby_landmark_id')
    name = request.POST.get('name')
    status = request.POST.get('status')

    if nearby_landmark_id:
        nearby_landmark_qs = Nearby_Landmark.objects.get(id=int(nearby_landmark_id), deleted=False)
        nearby_landmark_qs.name = name
        nearby_landmark_qs.status = status
        nearby_landmark_qs.save()
    else:
        nearby_landmark = Nearby_Landmark(name=name, status=status)
        nearby_landmark.save()
    return redirect("aragonapp:nearby_landmark_list")

def nearby_landmark_delete(request):
    nearby_landmark_id = request.GET.get('id')
    if nearby_landmark_id:
        nearby_landmark = Nearby_Landmark.objects.get(id=nearby_landmark_id)
        nearby_landmark.deleted = True
        nearby_landmark.save()
        return redirect("aragonapp:nearby_landmark_list")

def package_list(request):
    package_id = request.GET.get('id')
    package_one = []
    if package_id:
        package_one = Package.objects.get(id=package_id, deleted=False)
    packages = Package.objects.filter(deleted=False).order_by('package_name')
    for package in packages:
        if package.status == True:
            package.status = "Active"
        else:
            package.status = "Inactive"
    return render(request, "package/package_list.html",
                  {'packages': packages, 'package_one': package_one})

def package_view(request):
    package_id = request.GET.get('id')
    package_one = []
    if package_id:
        package_one = Package.objects.get(id=package_id, deleted=False)
    packages = Package.objects.filter(deleted=False).order_by('package_name')
    for package in packages:
        if package.status == True:
            package.status = "Active"
        else:
            package.status = "Inactive"
    return render(request, "package/package_view.html",
                  {'packages': packages, 'package_one': package_one})

def package_add(request):
    package_id = request.GET.get('id')
    package_qs = []
    if package_id:
        package_qs = Package.objects.get(id=int(package_id), deleted=False)
    return render(request, 'package/package_add.html', {'package_qs': package_qs})

def package_edit(request):
    package_id = request.POST.get('package_id')
    package_name = request.POST.get('package_name')
    package_price = request.POST.get('package_price')
    package_life = request.POST.get('package_life')
    package_type = request.POST.get('package_type')
    applicable_for = request.POST.get('applicable_for')
    status = request.POST.get('status')

    if package_id:
        package_qs = Package.objects.get(id=int(package_id), deleted=False)
        package_qs.package_name = package_name
        package_qs.package_price = package_price
        package_qs.package_life = package_life
        package_qs.package_type = package_type
        package_qs.applicable_for = applicable_for
        package_qs.status = status
        package_qs.save()
    else:
        package = Package(package_name=package_name, package_price=package_price, package_life=package_life,
                          package_type=package_type, applicable_for=applicable_for, status=status)
        package.save()
    return redirect("aragonapp:package_list")

def package_delete(request):
    package_id = request.GET.get('id')
    if package_id:
        package = Package.objects.get(id=package_id)
        package.deleted = True
        package.save()
        return redirect("aragonapp:package_list")

def property_types_view(request):
    property_types_id = request.GET.get('id')
    property_types_one = []
    if property_types_id:
        property_types_one = Property_types.objects.get(id=property_types_id)
    property_types = Property_types.objects.filter(deleted=False).order_by('name')
    if property_types_one.status == True:
        property_types_one.status = "Active"
    else:
        property_types_one.status = "Inactive"
    return render(request, "property_types/property_types_view.html",
                  {'property_types': property_types, 'property_types_one': property_types_one})

def property_types_list(request):
    property_types_id = request.GET.get('id')
    property_types_one = []
    if property_types_id:
        property_types_one = Property_types.objects.get(id=property_types_id)
    property_types = Property_types.objects.filter(deleted=False).order_by('name')
    for property_type in property_types:
        if property_type.status == True:
            property_type.status = "Active"
        else:
            property_type.status = "Inactive"
    return render(request, "property_types/property_types_list.html",
                  {'property_types': property_types, 'property_types_one': property_types_one})

def property_types_add(request):
    property_types_id = request.GET.get('id')
    property_types_qs = []
    if property_types_id:
        property_types_qs = Property_types.objects.get(id=int(property_types_id), deleted=False)
    return render(request, 'property_types/property_types_add.html', {'property_types_qs': property_types_qs})

def property_types_edit(request):
    property_types_id = request.POST.get('property_types_id')
    property_type = request.POST.get('name')
    status = request.POST.get('status')
    if property_types_id:
        property_types_qs = Property_types.objects.get(id=int(property_types_id), deleted=False)
        property_types_qs.name = property_type
        property_types_qs.status = status
        property_types_qs.save()
    else:
        property_types = Property_types(name=property_type, status=status)
        property_types.save()
    return redirect("aragonapp:property_types_list")

def property_types_delete(request):
    property_types_id = request.GET.get('id')
    if property_types_id:
        property_types = Property_for.objects.get(id=property_types_id)
        property_types.deleted = True
        property_types.save()
        return redirect("aragonapp:property_types_list")

def property_for_view(request):
    property_for_id = request.GET.get('id')
    property_for_one = []
    if property_for_id:
        property_for_one = Property_types.objects.get(id=property_for_id)
    property_for = Property_types.objects.filter(deleted=False).order_by('name')
    if property_for_one.status == True:
        property_for_one.status = "Active"
    else:
        property_for_one.status = "Inactive"
    return render(request, "property_for/property_for_view.html",
                  {'property_for': property_for, 'property_for_one': property_for_one})

def property_for_list(request):
    property_for_id = request.GET.get('id')
    property_for_one = []
    if property_for_id:
        property_for_one = Property_for.objects.get(id=property_for_id)
    property_for = Property_for.objects.filter(deleted=False).order_by('name')
    for property in property_for:
        if property.status == True:
            property.status = "Active"
        else:
            property.status = "Inactive"
    return render(request, "property_for/property_for_list.html",
                  {'property_for': property_for, 'property_for_one': property_for_one})

def property_for_add(request):
    property_for_id = request.GET.get('id')
    property_for_qs = []
    if property_for_id:
        property_for_qs = Property_for.objects.get(id=int(property_for_id), deleted=False)
    return render(request, 'property_for/property_for_add.html', {'property_for_qs': property_for_qs})

def property_for_edit(request):
    property_for_id = request.POST.get('property_for_id')
    property_for = request.POST.get('name')
    status = request.POST.get('status')
    if property_for_id:
        property_for_qs = Property_for.objects.get(id=int(property_for_id), deleted=False)
        property_for_qs.name = property_for
        property_for_qs.status = status
        property_for_qs.save()
    else:
        property_for = Property_for(name=property_for, status=status)
        property_for.save()
    return redirect("aragonapp:property_for_list")

def property_for_delete(request):
    property_for_id = request.GET.get('id')
    if property_for_id:
        property_for = Property_for.objects.get(id=property_for_id)
        property_for.deleted = True
        property_for.save()
        return redirect("aragonapp:property_for_list")
