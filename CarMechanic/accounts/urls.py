from django.contrib.auth.views import LoginView
from django.urls import path

from CarMechanic.accounts.views import HomePage

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', HomePage.as_view(), name='home'),
]