from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')    

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio', 'get_fabricacion_year',
                'p_costo', 'p_venta')
    ordering = ("nombre","laboratorio")
    list_display_links = ('nombre','laboratorio')
    list_filter = ('laboratorio','nombre')
    search_fields = ('nombre', 'laboratorio__nombre')
    
    def get_fabricacion_year(self, obj):
        return obj.f_fabricacion.year
    get_fabricacion_year.short_description = 'Año de fabricación'

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorAdmin)
admin.site.register(Producto,ProductoAdmin)

