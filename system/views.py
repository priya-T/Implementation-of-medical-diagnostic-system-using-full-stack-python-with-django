from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect) 
from easy_pdf.views import PDFTemplateResponseMixin
from django.views import generic
from django.views.generic import DetailView
from system.models import Doctor
from django.template import Template, Context 
from django.shortcuts import  render, redirect,HttpResponseRedirect
from system.forms import SignUpForm,AppointmentForm,Appointment1Form
from system.forms import TestreportForm,DoctorForm, ProfileForm,TestreportForm1
from django.contrib.auth import  login as dj_login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from system.contact import ContactForm
from django.core.mail import send_mail, get_connection
import io
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from . import forms,models
from system.models import Doctor,Profile,Test,Appointment,Testreport


def password_reset(request):
    return render(request, 'registration/password_reset_form.html')

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')

def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def Contact(request):
     submitted = False
     if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
            cd = form.cleaned_data
             # assert False
             
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(cd['subject'],cd['message'],cd.get('email', 'pt770034@gmail.com'),
                 ['pt770032@gmail.com'],
                 connection=con)
            return HttpResponseRedirect('/contact?submitted=True')
     else:
         form = ContactForm()
         if 'submitted' in request.GET:
             submitted = True
 
     return render(request, 'contact.html', {'form': form, 'submitted': submitted})

def logout(request):
	#messages.info(request, "You have successfully logged out.") 
	return render(request,'logout.html')

def plogout(request):
	#messages.info(request, "You have successfully logged out.") 
	return render(request,'plogout.html')

def login(request):
	submitted=False
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				dj_login(request,user)
				return render(request,'base2.html')
				#messages.info(request, f"You are now logged in as {username}.")
				#return render(request,'base2.html')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	if 'submitted' in request.GET:
            submitted = True
	return render(request=request, template_name="login.html", context={"login_form":form})

def plogin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user.is_superuser is False:
				dj_login(request,user)
				#messages.info(request, f"You are now logged in as {username}.")
				return render(request,'base3.html')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="plogin.html", context={"plogin_form":form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.location = form.cleaned_data.get('location')
            user.profile.mobile = form.cleaned_data.get('mobile')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            dj_login(request, user)
            return render(request,'success.html')  
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm
    return render (request=request, template_name="signup.html", context={"register_form":form})

def showp(request):  
    profiles= Profile.objects.all()  
    return render(request,"showp.html",{'profiles':profiles})  

def doctor(request):  
    if request.method == "POST":  
        form = DoctorForm(request.POST, request.FILES) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = DoctorForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    doctors= Doctor.objects.all()  
    return render(request,"show.html",{'doctors':doctors})

def showd(request):  
    doctors= Doctor.objects.all()  
    return render(request,"showd.html",{'doctors':doctors})

def edit(request, id):  
    doctor =Doctor.objects.get(id=id)  
    return render(request,'edit.html', {'doctor':doctor})

def update(request, id):  
    doc= Doctor.objects.get(id=id)  
    form = DoctorForm(request.POST,request.FILES, instance = doc)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'doc': doc})  

def destroy(request, id):  
    doc = Doctor.objects.get(id=id)  
    doc.delete()  
    return redirect("/show")  


class TestListView(generic.ListView):
    model =Test
    template_name = 'Test.html'

def appointment(request):  
    if request.method == "POST":  
        form = AppointmentForm(request.POST) 
        if form.is_valid(): 
            try:  
                form.save()  
                return redirect('/showa')  
            except:  
                pass  
    else:  
        form = AppointmentForm()  
    return render(request,'indexa.html',{'form':form})   

def showa(request):  
    appointments= Appointment.objects.all().filter(PatientId=request.user.id)  
    return render(request,"showa.html",{'appointments':appointments})

def showapp(request):  
    appointments= Appointment.objects.all()  
    return render(request,"showapp.html",{'appointments':appointments})

def edita(request, id):  
    appointment =Appointment.objects.get(id=id)  
    return render(request,'edita.html', {'appointment':appointment})

def updatea(request, id):  
    app= Appointment.objects.get(id=id)  
    form = Appointment1Form(request.POST, instance = app)  
    if form.is_valid():  
        form.save()  
        return redirect("/showapp")  
    return render(request, 'edita.html', {'app': app})  

def destroya(request, id):  
    app = Appointment.objects.get(id=id)  
    app.delete()  
    return redirect("/showa")

class DoctorDetailView(generic.DetailView):    
    model = Doctor    
    template_name = 'doctor_detail.html'

class PdfDetail(PDFTemplateResponseMixin,DetailView):        
    template_name = 'pdf_detail.html'
    context_object_name='obj'
    model = Testreport

def testreport(request):  
    if request.method == "POST":  
        form = TestreportForm(request.POST, request.FILES) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showr')  
            except:  
                pass  
    else:  
        form = TestreportForm()  
    return render(request,'indexr.html',{'form':form})  

def showr(request):  
    testreports= Testreport.objects.all()  
    return render(request,"showr.html",{'testreports':testreports})

def editr(request, id):  
    testreport =Testreport.objects.get(id=id)  
    return render(request,'editr.html', {'testreport':testreport})

def updater(request, id):  
    testreport= Testreport.objects.get(id=id)  
    form = TestreportForm1(request.POST, instance = testreport)  
    if form.is_valid():  
        form.save()  
        return redirect("/showr")  
    return render(request, 'editr.html', {'testreport': testreport})  

def destroyr(request, id):  
    testreport = Testreport.objects.get(id=id)  
    testreport.delete()  
    return redirect("/showr")  

def showrep(request):  
    testreports= Testreport.objects.all().filter(patientId=request.user.id)    
    return render(request,"showrep.html",{'testreports':testreports})