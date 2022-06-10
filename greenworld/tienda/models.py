import email
from django.db import models

class Producto(models.Model):
    prod_nombre = models.CharField(max_length=50)
    prod_precio = models.IntegerField()
    prod_descripcion = models.TextField()
    prod_stock = models.IntegerField()
    prod_img = models.ImageField(upload_to='productos/', null=True, blank=True)
    #prod_fecha = models.DateField()

    def __str__(self):
        return self.prod_nombre



