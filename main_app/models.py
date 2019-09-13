from django.db import models

class Trip(models.Model):
  city = models.CharField(max_length=56)
  country = models.CharField(max_length=100)
  arrival = models.DateField
  departure = models.DateField

  def __str__(self):
    return self.city




# c = Trip(city='Tokyo', country='Japan', arrival='April', departure='April')