from django.shortcuts import render
from .models import Trip



# trips = [
#   Trip('Tokyo', 'Japan', '4/3/2019', '4/20/2019'),
#   Trip('Punta Cana', 'Dominican Republic', '10/27/2018', '11/11/2018'),
#   Trip('Prague', 'Czechia', '5/19/2018', '6/1/2018')
# ]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trips_index(request):
  trips = Trip.objects.all()
  return render(request, 'trips/index.html', { 'trips': trips })

def trips_detail(request):
  trip = Trip.objects.get(id=trip_id)
  return render(request, 'trips/detail.html', { 'trip': trip })