from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from CarMechanic.buses.forms import BusForm
from CarMechanic.buses.models import Bus, Modifications
from CarMechanic.docxgeneration.models import RepairSession
from CarMechanic.mixins import CheckForRestriction


# Create your views here.


class BusListView(CheckForRestriction, ListView):

    model = Bus
    template_name = 'buses/bus-list.html'
    context_object_name = 'buses'


class BusAddView(CheckForRestriction, CreateView):

    model = Bus
    form_class = BusForm
    template_name = 'buses/create-bus.html'
    success_url = reverse_lazy('bus_list')


class BusDeleteView(CheckForRestriction, DeleteView):

    model = Bus
    template_name = 'buses/delete-bus.html'
    success_url = reverse_lazy('bus_list')


class BusDetailView(CheckForRestriction, DetailView):

    model = Bus
    template_name = 'buses/detail-bus.html'


class BusUpdateView(CheckForRestriction, UpdateView):

    model = Bus
    template_name = 'buses/edit-bus.html'
    form_class = BusForm

    def get_success_url(self):
        return reverse_lazy('bus_list')


class BusRepairListView(CheckForRestriction, ListView):
    model = RepairSession
    template_name = 'repairs/repair-list.html'
    context_object_name = 'repairs'  # This will be used in the template
    paginate_by = 5

    def get_queryset(self):
        # Get the bus by the ID passed in the URL
        bus = get_object_or_404(Bus, pk=self.kwargs['bus_id'])

        # Get all repair sessions for the bus
        return RepairSession.objects.filter(bus=bus)

    def get_context_data(self, **kwargs):
        # Get the default context data
        context = super().get_context_data(**kwargs)

        # Get the bus object again for the context
        bus = get_object_or_404(Bus, pk=self.kwargs['bus_id'])

        # Add the bus object to the context
        context['bus'] = bus

        return context


class RepairDetailView(CheckForRestriction, DetailView):
    model = RepairSession
    template_name = 'repairs/repair-detail.html'
    context_object_name = 'repair_session'  # Make it clear that this is a RepairSession object

    def get_context_data(self, **kwargs):
        # Get the default context data
        context = super().get_context_data(**kwargs)

        # Get the current `RepairSession` object
        repair_session = self.get_object()

        # Add additional context for the session
        context['repair_session'] = repair_session  # Add the repair session itself
        context['bus'] = repair_session.bus  # Add the associated bus
        context['modifications'] = repair_session.modifications.all()  # Add the related modifications (repairs)

        return context

