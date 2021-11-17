from django.urls import path 
from .views import *

urlpatterns = [ 
    path("",getRoutes,name="source"),
    path("notes/",getNotes,name="notes"),
    path("notes/<str:pk>/",getNote,name="note")
]