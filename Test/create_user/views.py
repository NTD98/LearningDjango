from django.shortcuts import render
from create_user.forms import UserProfileInfoForm,UserForm

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'create_user/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    registered = False
    user_form = UserForm()
    profile_form = UserProfileInfoForm()
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user = UserForm()
        profile = UserProfileInfoForm()

    return render(request,'create_user/registration.html',
                                                        {'user_form':user_form,
                                                         'userinfo_form':profile_form,
                                                         'registered':registered})
        
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("USERNAME :{} , PASSWORD: {} ".format(username,password))
            return HttpResponse("invalid user info!")
    else:
        return render(request,"create_user/login.html",{})