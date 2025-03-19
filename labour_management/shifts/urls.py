from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shifts_index"),
    path("rota/<str:date>/<str:shift_type>/", views.manning_rota, name="manning_rota"),
]
