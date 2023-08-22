from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    ordering = ("id",)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "laboratorio")
    ordering = ("nombre",)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "laboratorio", "f_year", "p_costo", "p_venta")
    ordering = ("nombre", "laboratorio")
    list_display_links = ("nombre", "laboratorio")
    list_filter = ("nombre", "laboratorio")

    def f_year(self, obj):
        return obj.f_fabricacion.year
    
    f_year.short_description = "F Fabricación"


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
