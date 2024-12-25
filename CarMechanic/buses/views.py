from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from CarMechanic.buses.forms import BusForm
from CarMechanic.buses.models import Bus, Modifications
from CarMechanic.repairs.models import RepairSession
from CarMechanic.mixins import CheckForRestriction


# Create your views here.


class BusListView(ListView):

    model = Bus
    template_name = 'buses/bus-list.html'
    context_object_name = 'buses'
    paginate_by = 12

    def get_queryset(self):

        queryset = super().get_queryset()
        query = self.request.GET.get('q')  # Get the search query from the request

        if query:
            queryset = queryset.filter(Q(model__icontains=query) | Q(number__icontains=query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')  # Add the search query to the context
        return context


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


