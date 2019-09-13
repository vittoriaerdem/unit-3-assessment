from django.db import models
from django.urls import reverse

class Trip(models.Model):
  city = models.CharField(max_length=56)
  country = models.CharField(max_length=100)
  arrived = models.CharField(max_length=10)
  departed = models.CharField(max_length=10)

  def __str__(self):
    return self.city

  def get_absolute_url(self):
    return reverse('detail', kwargs={'trip_id': self.id})


# c = Trip(city='Tokyo', country='Japan', arrival='April', departure='April')