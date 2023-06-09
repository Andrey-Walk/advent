from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('transport', views.transport, name='transport'),
    path('prog', views.prog, name='prog'),
    path('prog2', views.prog2, name='prog2'),
    path('prog3', views.prog3, name='prog3'),
    path('prog4', views.prog4, name='prog4'),
    path('prog5', views.prog5, name='prog5'),
    path('prog6', views.prog6, name = 'prog6'),
    path('prog7', views.prog7, name = 'prog7'),
    path('prog8', views.prog8, name = 'prog8'),
    path('prog9', views.prog9, name = 'prog9'),
    path('prog10', views.prog10, name = 'prog10')
]