from django.urls import path
from django.urls.conf import include

from CarMechanic.buses.views import BusListView, BusAddView, BusDeleteView, BusDetailView, BusUpdateView, \
    BusRepairListView, RepairDetailView

urlpatterns = [
    path('', BusListView.as_view(), name='bus_list'),
    path('create/', BusAddView.as_view(), name='bus_create'),
    path('<int:pk>/', include([
        path('detail/', BusDetailView.as_view(), name='bus_detail'),
        path('delete/', BusDeleteView.as_view(), name='bus_delete'),
        path('edit/', BusUpdateView.as_view(), name='bus_edit'),
    ])),
    path('bus/<int:bus_id>/repairs/', BusRepairListView.as_view(), name='bus_repairs'),
    path('repair/<int:pk>/', RepairDetailView.as_view(), name='repair_detail'),
]