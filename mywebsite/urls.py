from django.urls import path
from mywebsite import views
from . import views

urlpatterns = [
    path('', views.home),

]