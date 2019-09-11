from django.db import models

class Trip:  # Note that parens are optional if not inheriting from another class
  def __init__(self, city, country, arrival, departure):
    self.city = city
    self.country = country
    self.arrival = arrival
    self.departure = departure

trips = [
  Trip('Tokyo', 'Japan', '4/3/2019', '4/20/2019'),
  Trip('Punta Cana', 'Dominican Republic', '10/27/2018', '11/11/2018'),
  Trip('Prague', 'Czechia', '5/19/2018', '6/1/2018')
]