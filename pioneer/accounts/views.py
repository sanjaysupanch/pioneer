from django.shortcuts import render,redirect, HttpResponse
from accounts.forms import add_registration_form,RegistrationForm, ChangeProfileForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def index(request):
    return render(request,'accounts/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        profile_form = add_registration_form(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'image' in request.FILES:
                print('found it')
                profile.image = request.FILES['image']
            profile.save()
            registered = True
            return redirect("/")
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = RegistrationForm()
        profile_form = add_registration_form()
    return render(request,'accounts/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Your account was inactive.")
#         else:
#             print("Someone tried to login and failed.")
#             print("They used username: {} and password: {}".format(username,password))
#             return HttpResponse("Invalid login details given")
#     else:
#         return render(request, 'accounts/login.html', {})

@login_required
def view_profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user
    args={'user':user}
    return render(request,'accounts/profile.html',args)

@login_required
def edit_profile(request):        #edit profile view
    if request.method=='POST':
        form=EditProfileForm(request.POST, instance=request.user)
        form1 = ChangeProfileForm(request.POST, instance=request.user)
        if form.is_valid() and form1.is_valid():
            form.save()
            UserProfile.objects.filter(user=request.user).update(city=request.POST['city'])
            UserProfile.objects.filter(user=request.user).update(phone=request.POST['phone'])
            # UserProfile.objects.filter(user=request.user).update(image=request.POST['image'])

            return redirect('/accounts/profile')
        # else:
        #     return HttpResponse("form  is invalid")

    else:
        form=EditProfileForm(instance=request.user)
        form1=ChangeProfileForm(request.POST,instance=request.user)
        args={'form':form, 'form1':form1}
        return render(request,'accounts/edit_profile.html', args)


@login_required
def change_password(request):        #change password view
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')

    else:
        form=PasswordChangeForm(user=request.user)

        args={'form':form}
        return render(request,'accounts/change_password.html',args)


