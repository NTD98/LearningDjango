from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'basic_form'
#url-mapping
urlpatterns = [
    url(r'^$' , views.index, name='index'),
    url(r'^formview/',views.form_view,name='form_view')
]
