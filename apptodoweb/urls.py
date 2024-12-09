from django.urls import path
from . import views

App_name = "apptodoweb"

urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
]