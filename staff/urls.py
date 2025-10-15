from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_staff", views.create_staff, name="create_staff"),
    path("login", views.login, name="login"),
    path("create_location", views.create_location, name="create_location"),
    path("create_activity", views.create_activity, name="create_activity")
]