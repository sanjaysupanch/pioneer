from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.validators import validate_email

class RegistrationForm(forms.ModelForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username.'}), required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email ID.'}), required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter firstname.'}), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter lastname.'}), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password.'}), required=True, max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter confirm password.'}), required=True, max_length=50)


    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

#     def clean_username(self):
#         user = self.clean_data['username']
#         try:
#             match = User.objects.get(username = user)
#         except:
#             return self.cleaned_data['username']
#         raise forms.ValidationError("Username already exist")

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         try:
#             mt = validate_email(email)
#         except:
#             return forms.ValidationError("Email is not correct format")
#         return email
        
    def clean_confirm_password(self):
        pas = self.cleaned_data['password']
        cpas = self.cleaned_data['confirm_password']
        MIN_LENGTH = 6
        if pas and cpas:
            if pas!=cpas:
                raise forms.ValidationError('password and confirm password not matched')
            else:
                if len(pas) < MIN_LENGTH:
                    raise forms.ValidationError("Password should have atleast %d character " % MIN_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError("Password should not all numeric")

class add_registration_form(forms.ModelForm):
    city  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter city name.'}), required=True, max_length=50)
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Mobile number.'}),required=True)
    #image = forms.ImageField()
    class Meta:
        model = UserProfile
        fields=['city', 'phone', 'image']

    # def clean_phone(self):
    #     LENGTH = 10
    #     if phone != LENGTH :
    #         raise forms.ValidationError("Enter a valid mobile number") 

class EditProfileForm(UserChangeForm):  #our own custom edit profile form
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter email ID.'}), required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter firstname.'}), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter lastname.'}), required=True, max_length=50)
    #password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password.'}), required=True, max_length=50)
    
    class Meta:
        model=User
        fields = ('email', 'first_name', 'last_name', 'password')

class ChangeProfileForm(forms.ModelForm):  #our own custom edit profile form
    city  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter city name.'}), required=True, max_length=50)
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Mobile number.'}),required=True)
    
    class Meta:
        model=UserProfile
        fields=('phone', 'city', 'image')