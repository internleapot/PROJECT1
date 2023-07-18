"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls import static

app_name = "elearn"
urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('otp/', views.otp, name="otp"),
    path('employerprofile/', views.employerprofile, name="employerprofile"),
    path('profileform/', views.profileform, name="profileform"),
    path('edit/', views.edit, name="edit"),
    path('hodprofile/', views.hodprofile, name="hodprofile"),
    path('employeenmbr/',views.employeenmbr, name="employeenmbr"),
    path('addemployee/',views.addemployee, name="addemployee"),
    path('mainrepresentative/', views.mainrepresentative, name="mainrepresentative"),
    path('profileinfo/', views.profileinfo, name="profileinfo"),
    path('companydashboard/', views.companydashboard, name="companydashboard"),
    path('table/', views.table, name="table"),
    path('maindashboard/', views.maindashboard, name="maindashboard"),
    path('departments/', views.departments, name="departments"),
    path('projects/', views.projects, name="projects"),
    path('notifications/', views.notifications, name="notifications"),
    path('admindashboard/', views.admindashboard, name="admindashboard"),
    path('base/', views.base, name="base"),
]

