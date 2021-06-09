from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.forms import ModelForm
from system.models import Testreport, Appointment, Doctor, Profile
  

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=500)
    last_name = forms.CharField(max_length=500)
    bio = forms.CharField(max_length=500)
    location = forms.CharField(max_length=30)
    mobile = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'birth_date', 'password1', 'password2','bio','location','mobile' )

def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class AppointmentForm(ModelForm):
      required_css_class = 'required'
      class Meta:
          model = Appointment
          fields =['PatientId','patientName','description','doctorId']

class TestreportForm(ModelForm):
      required_css_class = 'required'
      class Meta:
          model =Testreport
          fields = '__all__'

class TestreportForm1(ModelForm):
      required_css_class = 'required'
      class Meta:
          model =Testreport
          fields = ['OtherCharge','Test_result','total']

class DoctorForm(ModelForm):
      required_css_class = 'required'
      class Meta:
          model = Doctor
          fields = '__all__'

class ProfileForm(forms.ModelForm):
      required_css_class = 'required'
      class Meta:
          model = Profile
          fields = '__all__'

class Appointment1Form(ModelForm):
      required_css_class = 'required'
      class Meta:
          model = Appointment
          fields =['status']