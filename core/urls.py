from django.urls import path, include
from .views import *
from . import views
from django.contrib import admin

urlpatterns = [
    path('', index, name="index"),
    path('prediction/', WinePredict, name="winepredict"),
    path('output/', Output, name="output"),
    path('report/', Report, name="report"),
    path('visual/', visual, name="age"),
    path('visual/age', views.age),
    path('visual/gender', views.gender),
    path('visual/chest', views.chest),
    path('visual/blood', views.blood),
    path('visual/cholestoral', views.cholestoral),
    path('visual/fasting', views.fasting),
    path('visual/electrocardiographic', views.electrocardiographic),
    path('visual/heartRate', views.heartRate),
    path('visual/exercise', views.exercise),
    path('visual/st', views.st),
    path('visual/vessels', views.vessels),
    path('visual/thalassemia', views.thalassemia),
    path('login/', views.login, name="login"),
    # path('users/', include('core.urls')),
    # path((r'^$', users, name="users"),
    path('register', views.register, name='register'),
    path('registerDB', views.registerDB),
    path('login', views.login),
    path('login_check', views.login_check),
    path('logout', views.logout, name='logout'),
    path('know-more/', know_more, name="know_more"),
    path('databases/', databases, name="databases"),
    path('healthy/', healthy, name='healthy'),
    path('unhealthy/', unhealthy, name='unhealthy'),
    path('data_proc_report/', data_proc_report, name="data_proc_report"),
    path('about/', about, name="about"),
    path('databases/delete/<int:id>', views.delete, name="delete"),
    # path('404', views.page_not_found, name="404")

]
