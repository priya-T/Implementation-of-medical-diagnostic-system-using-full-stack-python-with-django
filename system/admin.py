from django.contrib import admin
from .models import Appointment, Test,Testreport,Doctor,Profile

# Register your models here.



@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ( 'Doctor_name', 'profile_pic','address','mobile','department')
    ordering = ('Doctor_name','department')
    search_fields = ('Doctor_name','mobile')
    list_filter = ('Doctor_name','mobile')
    fieldsets = (
         ('Required Information', {
              'description': "These fields are required for each event.",
            'fields': (('Doctor_name'),'profile_pic','address','mobile','department' )
         }),
        
    )

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('PatientId','patientName','doctorId','appointmentDate','description','status')





class TestAdmin(admin.ModelAdmin):
    list_display = ( 'Test_name','Test_fee','Test_type')


class TestreportAdmin(admin.ModelAdmin):
    list_display = ('patientId',
    'DoctorId',
    'appointmentId',
    'test', 
    'Test_result',
    'OtherCharge',
    'total')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user',
    'bio', 
    'location',
    'mobile', 
    'birth_date')

admin.site.register(Appointment)
admin.site.register(Profile)
admin.site.register(Test)
admin.site.register(Testreport)

