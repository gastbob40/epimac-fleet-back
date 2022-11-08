# Create your views here.
from django.http import JsonResponse

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
    } for imac in imacs]

    return JsonResponse({
        "imacs": formatted_imacs
    })
