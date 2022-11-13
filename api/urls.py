from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("imacs", views.get_imacs),
    path("imacs/<int:mac_id>", views.get_imac),
    path("auth/login", csrf_exempt(views.check_auth_login)),
    path("auth/register", csrf_exempt(views.post_register_request)),
]