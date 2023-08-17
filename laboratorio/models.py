from django.db import models
from django.core.validators import ValidationError
from datetime import date
from django.urls import reverse

def validate_min_date(value):
    if value < date(2015, 1, 1):
        raise ValidationError('La fecha debe ser a partir de 2015.')
    
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=128)
    def __str__(self):
        return self.nombre
    
    def get_absoluted_url(self):
        return reverse('laboratorio', args=[str(self.id)])
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=128)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.PROTECT)

class Producto(models.Model):
    nombre = models.CharField(max_length=128)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT)
    f_fabricacion = models.DateField(validators=[validate_min_date])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)


