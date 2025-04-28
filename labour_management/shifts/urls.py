from django.urls import path
from . import views

urlpatterns = [
    path('',            views.index,        name='shifts_index'),
    path('<str:date>/',  views.manning_rota, name='manning_rota'),
]
