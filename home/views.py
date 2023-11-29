from django.shortcuts import render

# Create your views here.
from django.views.generic import Template



    
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from db_app.forms import charities_form # importing the charities model form


# Create your views here.
def index(request):
    """"a view to return the index page"""
    return render(request,'home/index.html')