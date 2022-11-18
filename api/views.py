# Create your views here.
import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from daemon.models import IMacModel
from daemon.utils.notification import send_register_request_notification


def get_imacs(request):
    imacs = IMacModel.objects.all()

    formatted_imacs = [{
        "id": imac.id,
        "label": imac.label,
        "ip": imac.ip,
        "macos_version": imac.macos_version,
        "serial_number": imac.serial_number,
        "storage_capacity": imac.storage_capacity,
        "memory": imac.memory,
        "cpu_cores": imac.cpu_cores,
        "status": imac.status,
        "last_seen": imac.last_seen,
    } for imac in imacs]

    return JsonResponse({
        "imacs": formatted_imacs
    })


def get_imac(request, mac_id):
    mac = get_object_or_404(IMacModel, pk=mac_id)

    return JsonResponse({
        "id": mac.id,
        "label": mac.label,
        "ip": mac.ip,
        "report_status": mac.report_status,

        "serial_number": mac.serial_number,
        "storage_capacity": mac.storage_capacity,
        "memory": mac.memory,
        "cpu_cores": mac.cpu_cores,

        "macos_version": mac.macos_version,
        "macos_build_version": mac.macos_build_version,

        "mac_user": mac.mac_user,
        "status": mac.status,
        "last_seen": mac.last_seen,
    })


def check_auth_login(request):
    if request.method != "POST":
        return JsonResponse({
            "error": "Invalid request method"
        }, status=405)

    body = request.body.decode('utf-8')
    body = json.loads(body)

    email = body.get("email")
    password = body.get("password")

    User = get_user_model()

    user = User.objects.filter(email=email).first()

    if not user or not user.check_password(password):
        return JsonResponse({
            "error": "User not found"
        }, status=400)

    return JsonResponse({
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "is_superuser": user.is_superuser,
    })


def post_register_request(request):
    if request.method != "POST":
        return JsonResponse({
            "error": "Invalid request method"
        }, status=405)

    body = request.body.decode('utf-8')
    body = json.loads(body)

    email = body.get("email")
    explication = body.get("explication")

    if not email or not explication:
        return JsonResponse({
            "error": "Missing fields"
        }, status=400)

    send_register_request_notification(email, explication)

    return JsonResponse({
        "message": "Request sent"
    })


def post_check_user_exists(request):
    if request.method != "POST":
        return JsonResponse({
            "error": "Invalid request method"
        }, status=405)

    body = request.body.decode('utf-8')
    body = json.loads(body)

    email = body.get("email")

    if not email:
        return JsonResponse({
            "error": "Missing fields"
        }, status=400)

    user = get_user_model().objects.filter(email=email).first()

    if not user:
        return JsonResponse({
            "error": "User not found"
        }, status=400)

    return JsonResponse({
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "is_superuser": user.is_superuser,
    })

