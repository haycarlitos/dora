from django.contrib import admin
from .models import Client, License



class LicenseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Cliente', {'fields': ['client']}),
        ('ID de Licencia', {'fields': ['license_id']}),
        ('Tipo de Licencia', {'fields': ['license_type']}),
        ('Paquete', {'fields': ['package_name']}),
        ('Fecha de expiración', {'fields': ['expiration_date']}),
    ]

    list_display = ('license_type', 'expiration_date', 'is_expired')


class ChoiceInline(admin.TabularInline):
    model = License
    extra = 2

class ClientAdmin(admin.ModelAdmin):

    inlines = [ChoiceInline]


admin.site.register(License, LicenseAdmin)
admin.site.register(Client, ClientAdmin)
