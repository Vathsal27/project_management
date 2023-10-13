from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('project_id/<int:project_id>',views.project_details, name="project_details")
]