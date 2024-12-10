from django.urls import path
from . import views

App_name = "apptodoweb"

urlpatterns = [
    #path("", views.MainView.as_view(), name="index"),
    #path("view_addToDo/", views.view_addToDo, name="view_addToDo"),
    path("", views.index, name="index"),
    path('del/<str:item_id>', views.remove, name="del"),
]