# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from daemon.models import IMacModel


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