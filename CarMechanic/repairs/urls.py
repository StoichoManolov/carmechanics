from django.urls import path

from CarMechanic.repairs.views import generate_word_file, BusRepairListView, RepairDetailView

urlpatterns = [
    path('', generate_word_file, name='repair'),
    path('<int:bus_id>/repairs/', BusRepairListView.as_view(), name='bus_repairs'),
    path('repair/<int:pk>/', RepairDetailView.as_view(), name='repair_detail')
]