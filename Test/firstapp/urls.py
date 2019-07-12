from django.conf.urls import url
from django.contrib import admin
from firstapp import views
#url-mapping
urlpatterns = [
    url(r'^$' , views.index, name='index')
]
