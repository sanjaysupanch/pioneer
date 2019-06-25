from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User

def registration(request):
    if request.method == 'POST':
        form1 = RegistrationForm(request.POST)
        #form2 = add_registration_form(request.POST)
        if form1.is_valid(): #and form2.is_valid:
            username = form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            #phone = form1.cleaned_data['phone']
            #city = form1.cleaned_data['city']
            #image = form1.cleaned_data['image']
            User.objects.create_user(username=username, first_name=first_name, last_name= last_name, email=email, password=password,) #phone=phone, city=city, image=image)
            return HttpResponseRedirect('/register/')
        
        else:
            form1 = RegistrationForm()
        return render(request, 'accounts/registration.html', {'form1':form1})