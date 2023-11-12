from django.urls import path
from resulapp import views

urlpatterns = [

    path('',views.index),
    path('about/',views.about)
]
