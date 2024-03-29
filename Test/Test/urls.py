"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from firstapp import views
from basicform import views as basic_form_view
from create_user import views as create_user_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^firstapp/',include('firstapp.urls')),
    url(r'^$',create_user_view.index,name='index'),
    url(r'^basicform/',include('basicform.urls')),
    url(r'^create_user/',include('create_user.urls')),
]
