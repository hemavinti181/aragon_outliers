from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from  django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate
from django.conf import settings
# Create your views here.
def index(request):

    user = User.objects.all()
    return render(request,"index.html",{'user':user})

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
def edit_user(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(id=id)

        user.name = name
        user.email = email
        user.password = password
        user.save()

        return redirect('/')

    else:
        user = User.objects.get(id=id)
        context = {
            'user': user,
        }
        return render(request, 'edit.html', context)
def delete_user(request, id):

    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')
def profile(request):
    return render(request,profile.html)