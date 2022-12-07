from http.client import ImproperConnectionState
import imp
from operator import index
from django.urls import path
from planning.views import indexApp

urlpatterns = [
    path('', indexApp, name="indexApp")
]