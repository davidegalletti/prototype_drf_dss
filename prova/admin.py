from django.contrib import admin
from prova.models import Regione, Provincia


class ProvinciaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Regione)

