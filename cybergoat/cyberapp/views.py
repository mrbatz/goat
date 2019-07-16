import requests
from django.shortcuts import render
from cyberapp.forms import UserForm
from django.contrib.auth.models import User

from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from cyberapp.code import geo, news, alfred



def user_login(request):
    context={'title':news.title, 'image':news.image, 'ip':geo.ip, 'news_description':news.description,\
'url':news.url}

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


def prices(request):

    if request.method == "POST":
        quote = request.POST['quote'].upper()
        notfound = "Oops..Something went wrong. Please go back and try again."

        #get json request of crypto prices

        try:
            symbol = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD'.format(quote)).json()


            symbol_name= symbol['RAW']['{}'.format(quote)]['USD']['FROMSYMBOL']

            current_price= symbol['RAW']['{}'.format(quote)]['USD']['PRICE']
            current_price = '{:.2f}'.format(current_price)
            lowhour= symbol['RAW']['{}'.format(quote)]['USD']['LOWHOUR']
            lowhour = '{:.2f}'.format(lowhour)
            highhour= symbol['RAW']['{}'.format(quote)]['USD']['HIGHHOUR']
            highhour = '{:.2f}'.format(highhour)
            market = symbol['RAW']['{}'.format(quote)]['USD']['MARKET']
            return render(request, 'cyberapp/prices.html',{'symbol_name':symbol_name,
            'current_price':current_price, 'lowhour':lowhour, 'highhour':highhour, 'market':market})


        except KeyError:
                return render(request, 'cyberapp/prices.html', {'notfound':notfound})








    else:

        return render(request, 'cyberapp/prices.html', {'notfound':notfound})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))




@login_required
def home(request):


        #alfred = request.POST['alfred']


    return render(request, 'cyberapp/home.html',{})

@login_required
def tools(request):
    return render(request, 'cyberapp/tools.html', {})
