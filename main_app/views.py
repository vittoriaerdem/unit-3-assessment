from django.shortcuts import render

from .models import Trip
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')

def trips_index(request):
  return render(request, 'trips/index.html', { 'trips': trips })