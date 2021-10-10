

from django.urls import path
from . import views

urlpatterns = [
    path("",views.EmailSh,name='email'),
]
