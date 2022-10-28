from django.db import models


# Create your models here.

class IMacModel(models.Model):
    label = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)

    class Meta:
        verbose_name = "IMac"
        verbose_name_plural = "IMacs"
