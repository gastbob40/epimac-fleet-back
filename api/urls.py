from django.urls import path

from . import views

urlpatterns = [
    path("imacs", views.get_imacs),
    path("imacs/<int:mac_id>", views.get_imac),
]