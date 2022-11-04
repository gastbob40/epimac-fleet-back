from django.contrib import admin

from daemon.models import IMacModel


# Register your models here.

@admin.register(IMacModel)
class IMacModelAdmin(admin.ModelAdmin):
    list_display = ('label', 'ip', 'macos_version', 'memory', 'cpu_cores', 'last_seen',)
    # Override the name on the admin page
