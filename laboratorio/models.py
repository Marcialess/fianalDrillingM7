from django.db import models


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, default="Santiago")
    pais = models.CharField(max_length=50, default="Chile")

    def __str__(self):
        return self.nombre
        


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, default="-----")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 128)
    laboratorio = models.ForeignKey(Laboratorio, on_delete = models.PROTECT)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits = 12, decimal_places = 2)
    p_venta = models.DecimalField(max_digits = 12, decimal_places = 2)

    def __str__(self):
        return self.nombre