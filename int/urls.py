"""int URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from system import views
from django.contrib.auth import views as auth_views
from system.views import plogout,logout,login,register,home,plogin,Contact,about,update,destroya,edita
from system.views import show,doctor,edit,destroy,TestListView,showp,appointment,showa,showapp,updatea
from system.views import DoctorDetailView,showd,testreport,showr,editr,updater,destroyr,showrep,PdfDetail
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url





 


urlpatterns = [
    path("home/",home),
    path("about/",about),
    path('admin/', admin.site.urls),
    path("signup/",register),
    path("login/",login),
    path("logout/",logout),
    path("plogout/",plogout),
    path("plogin/",plogin),
    path("contact/",Contact),
    path("doctor",doctor),  
    path('show',show),  
    path('edit/<int:id>',edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>', destroy), 
    path("Test/",TestListView.as_view()),
    path('showp',showp), 
    path("appointment",appointment), 
    path('showa',showa),  
    path('deletea/<int:id>', destroya),
    path('showapp',showapp),
    path('showd',showd),
    path('edita/<int:id>',edita),  
    path('updatea/<int:id>', updatea),
    path('doctor/<int:pk>',DoctorDetailView.as_view()),
     path("testreport",testreport),  
    path('showr',showr),  
    path('editr/<int:id>',editr),  
    path('updater/<int:id>', updater),  
    path('deleter/<int:id>', destroyr), 
    path('showrep',showrep),
    path('<int:pk>',views.PdfDetail.as_view(),),
    path('admin/password_reset/',auth_views.PasswordResetView.as_view(),name='admin_password_reset'),    
    path('admin/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),     
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),     
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    url('^', include('django.contrib.auth.urls')),
   
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
