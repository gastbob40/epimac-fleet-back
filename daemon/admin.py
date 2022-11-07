from django.contrib import admin

from daemon.models import IMacModel


# Register your models here.

@admin.register(IMacModel)
class IMacModelAdmin(admin.ModelAdmin):
    list_display = ('label', 'ip', 'macos_version', 'memory', 'cpu_cores', 'last_seen')

    fieldsets = (
        ('Config', {
            'fields': ('label', 'ip', 'mac_user')
        }),
        ('Software properties', {
           'fields': ('macos_version', 'macos_build_version')
        }),
        ('Hardware properties', {
            'fields': ('storage_capacity', 'memory', 'cpu_cores',)
        }),
        ('Daemon', {
            'fields': ('last_seen', 'status')
        }),
    )
    # Override the name on the admin page
