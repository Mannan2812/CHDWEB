"""CHDWEB URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from homepage import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',include('homepage.urls')),
    url(r'^index.html',include('homepage.urls')),
    url(r'^destination.html',include('destination.urls')),
    url(r'^about.html',include('about.urls')),
    url(r'^blog.html',include('blog.urls')),
    url(r'^contact.html',include('contact.urls')),
    url(r'^dest1.html',include('lake.urls')),
    url(r'^bus_guide.html',include('busguide.urls')),
    url(r'^rock_garden.html',include('homepage.urls')),
    url(r'^sukhna_lake.html',include('homepage.urls')),
    url(r'^rose_garden.html',include('homepage.urls')),
    url(r'^elante_mall.html',include('homepage.urls')),
    url(r'^iskcon_temple.html',include('homepage.urls')),
    url(r'^pec.html',include('homepage.urls')),
    url(r'^buses.html',include('homepage.urls')),
    url(r'^e-ticket.html',include('eticket.urls')),
    url(r'^ticket.html',include('eticket.urls')),
]
