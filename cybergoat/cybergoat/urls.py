"""cybergoat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from cyberapp import views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'^home/$', views.home, name='home'),
    url(r'^$', views.user_login, name = 'user_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name ='register'),
    url(r'^budget/$', views.budget, name='budget'),

]
