from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")

class DirectorGeneralAdmin(admin.ModelAdmin):
    pass

class ProductoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
