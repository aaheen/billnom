from django.shortcuts import render
from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.conf.urls.i18n import i18n_patterns 

# Create your views here.
def indexbase(request):
    return render(request, 'billnom/index.html',{})

def retsumm(request):
    return render(request, 'billnom/billTex.html', {})
