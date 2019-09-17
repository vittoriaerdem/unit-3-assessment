from django.db import models
from django.urls import reverse

class Item(models.Model):
  description = models.CharField(max_length=100, default='DEFAULT VALUE')
  quantity = models.CharField(max_length=100, default='DEFAULT VALUE')

  def __str__(self):
    return self.description