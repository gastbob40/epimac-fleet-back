from django.db import models


# Create your models here.

class IMacModel(models.Model):
    # Config
    label = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    report_status = models.BooleanField(default=True)

    # Hardware properties
    serial_number = models.CharField(max_length=255)
    storage_capacity = models.FloatField()
    memory = models.IntegerField()
    cpu_cores = models.IntegerField()

    # Software properties
    macos_version = models.CharField(max_length=255)
    macos_build_version = models.CharField(max_length=255)

    # Daemon properties
    mac_user = models.CharField(max_length=255)
    last_seen = models.DateTimeField(null=True, blank=True)

    class MacStatus(models.TextChoices):
        UNAVAILABLE = "Unavailable"
        AVAILABLE = "Available"
        IN_USE = "In Use"

    status = models.CharField(
        max_length=255,
        choices=MacStatus.choices,
        default=MacStatus.UNAVAILABLE,
    )

    class Meta:
        verbose_name = "IMac"
        verbose_name_plural = "IMacs"

    def __str__(self):
        return self.label
