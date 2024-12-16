from django.urls import path
from . import views

urlpatterns = [
    path('receber-dados/', views.receber_dados, name='receber_dados'),
]
