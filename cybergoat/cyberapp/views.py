import requests
from django.shortcuts import render
from cyberapp.forms import UserForm
from django.contrib.auth.models import User

from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from cyberapp.code import news, cam




def user_login(request):
    context={'news_title':news.title, 'image':news.image, 'news_description':news.description,\
'url':news.url,'news_title2':news.title2, 'image2':news.image2, 'news_description2':news.description2,\
'ur2':news.url2, 'news_title3':news.title3, 'image3':news.image3, 'news_description3':news.description3,\
'url3':news.url3, 'cam':cam.image, 'cam_title':cam.title}

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and password: {}'.format(username, password))
            return HttpResponse('Invalid login details supplied!')



    else:
        return render(request, 'cyberapp/login.html', context)


@login_required
def register(request):
    registered = False

    if request.method =='POST':
        user_form = UserForm(data = request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile.user = user
            profile.save()

            registered= True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'cyberapp/registration.html',{'user_form': user_form, 'registered':registered})


def budget(request):
    return render(request, 'cyberapp/mybudget.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))




@login_required
def home(request):


        #alfred = request.POST['alfred']


    return render(request, 'cyberapp/home.html',{})
