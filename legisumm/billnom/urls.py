from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "billnom"

urlpatterns = [
    path('', views.indexbase, name='baseindex'),
    path('data', views.retsumm, name='baseindex'),

 ]

