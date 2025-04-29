from django.urls import path
from .views import SkillListView, SkillCreateView, SkillUpdateView, SkillDeleteView

urlpatterns = [
    path("",            SkillListView.as_view(),    name="skills_index"),
    path("add/",        SkillCreateView.as_view(),  name="skills_create"),
    path("<int:pk>/edit/",   SkillUpdateView.as_view(), name="skills_update"),
    path("<int:pk>/delete/", SkillDeleteView.as_view(), name="skills_delete"),
]
