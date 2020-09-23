from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("hello2/", views.hello2),
    path("hello3/", views.hello3),
]