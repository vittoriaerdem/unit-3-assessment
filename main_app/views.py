from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Item




def home(request):
  return render(request, 'index.html')

class ItemCreate(CreateView):
  model = Item
  fields = ['description', 'quantity']

  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    return super().form_valid(form)




class ItemDelete(DeleteView):
  model = Item
  success_url = '/home/'
