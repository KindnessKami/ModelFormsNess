from django.urls import path
from Modelapp import views

urlpatterns=[
    path('',views.index,name="index")
]