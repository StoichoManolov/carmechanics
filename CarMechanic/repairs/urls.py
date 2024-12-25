from django.urls import path

from CarMechanic.repairs.views import generate_word_file

urlpatterns = [
    path('', generate_word_file, name='repair')
]