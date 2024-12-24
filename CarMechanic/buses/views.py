from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from CarMechanic.buses.forms import BusForm
from CarMechanic.buses.models import Bus


# Create your views here.


class BusListView(ListView):

    model = Bus
    template_name = 'buses/bus-list.html'
    context_object_name = 'buses'


class BusAddView(CreateView):

    model = Bus
    form_class = BusForm
    template_name = 'buses/create-bus.html'
    success_url = reverse_lazy('bus_list')


class BusDeleteView(DeleteView):

    model = Bus
    template_name = 'buses/delete-bus.html'
    success_url = reverse_lazy('bus_list')


class BusDetailView(DetailView):

    model = Bus
    template_name = 'buses/detail-bus.html'


class BusUpdateView(UpdateView):

    model = Bus
    template_name = 'buses/edit-bus.html'
    form_class = BusForm

    def get_success_url(self):
        return reverse_lazy('bus_list')


