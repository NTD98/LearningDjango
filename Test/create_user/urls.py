from django.conf.urls import url
from django.contrib import admin
from create_user import views

app_name = 'create_user'
#url-mapping
urlpatterns = [
    url(r'^$' , views.index, name='index'),
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.user_login,name='login'),
    url(r'^logout/',views.user_logout,name='logout')
]
