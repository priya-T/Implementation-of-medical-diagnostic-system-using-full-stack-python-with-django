
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    mobile = models.CharField(max_length=20,null=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    def __str__(self):
          return  "%s :Patient ID" % self.id

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    

class Doctor(models.Model):
    Doctor_name=models.CharField(max_length=40)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50)
    def __str__(self):
          return  "%s :Doctor ID" % self.id

class Appointment(models.Model):
    PatientId=models.IntegerField(null=True)
    patientName=models.CharField(max_length=30,null=True)
    doctorId=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status = models.CharField(max_length=30,null=True)
    def __str__(self):
        return "%s :Appointment Id " % self.id

class Test(models.Model):
    Test_name = models.CharField(max_length=40)
    Test_fee = models.IntegerField()
    Test_type= models.CharField(max_length=40)

    def __str__(self):
        return "%s :Test Name" % self.Test_name

class Testreport(models.Model):
    patientId=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    DoctorId=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointmentId=models.ForeignKey(Appointment,on_delete=models.CASCADE)
    test= models.ForeignKey(Test,on_delete=models.CASCADE,null=True)
    Test_result = models.CharField(max_length=40)
    OtherCharge=models.IntegerField(null=False)
    total=models.IntegerField(null=False)
    def __str__(self):
        return "%s :Test Report Id" % self.id