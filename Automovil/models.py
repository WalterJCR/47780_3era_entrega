from django.db import models

# Create your models here.
class Auto(models.Model):
    # Atributos del auto
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    placa = models.CharField(max_length=10, unique=True)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # Método para obtener una representación textual del auto
    def _str_(self):
        return f"{self.marca} {self.modelo} {self.color} {self.placa}"
    

# Clase para representar un conductor
class Conductor(models.Model):
    # Atributos del conductor
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    licencia = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    # Método para obtener una representación textual del conductor
    def _str_(self):
        return f"{self.nombre} {self.dni} {self.licencia}"


# Clase para representar un alquiler de un auto por un conductor
class Alquiler(models.Model):
    # Atributos del alquiler
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    # Método para obtener una representación textual del alquiler
    def _str_(self):
        return f"{self.auto} alquilado por {self.conductor} desde {self.fecha_inicio} hasta {self.fecha_fin} por {self.costo}"

