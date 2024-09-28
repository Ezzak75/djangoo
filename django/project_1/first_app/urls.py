
from django.urls import path
from .views import course,about,home

urlpatterns = [

    
     path('course/',course),
     path('about/',about),
     path('',home),
]
