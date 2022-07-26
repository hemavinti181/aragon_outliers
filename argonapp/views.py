from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from  django.contrib.auth.models import User,auth
from .models import Country
from django.http import HttpResponse, JsonResponse

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
    country = Country.objects.all().order_by('country')
    return render(request, "country/country_list.html",
                  {'country': country, 'country_one': country_one})

def country_add(request):
    country_id = request.GET.get('id')
    country_qs = []
    if country_id:
        country_qs = Country.objects.get(id=int(country_id))
    return render(request, 'country/country_add.html', {'country_qs': country_qs})


def country_entry(request):
    print(Country.objects.all())
    id = request.POST.get('id')
    country = request.POST.get('country')
    status = request.POST.get('status')

    try:
        if id:
            country_qs = Country.objects.get(id=id)
            country = Country(id=country_qs.id, country=country, status=status)

        else:
            country = Country(country=country, status=status)

        country.save()

    except Exception as e:
        return JsonResponse({'msg': str(e)}, status=400)

    return redirect("country_view")


def country_delete(request):
    country_id = request.GET.get('id')
    if country_id:
        try:
            country = Country.objects.get(id=country_id)
            country.delete()
            return redirect("country_view")

        except Exception as e:
            return JsonResponse({'msg': str(e)}, status=400)
