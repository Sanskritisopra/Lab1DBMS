from django.urls import path
from . import views

urlpatterns = [
    path("front/",views.allinterns,name="front")
]
