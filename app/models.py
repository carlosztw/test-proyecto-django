from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=40)
    
    def __str__(self):
        return self.tipo

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True, upload_to= "productos")
    descripcion = models.CharField(max_length=60)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    fecha = models.DateField()
    
    def __str__(self):
        return self.nombre

consultas = [
    [0, "Consulta"],
    [1, "Reclamo"], 
    [2, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=consultas)
    mensaje = models.TextField(max_length=500)

    def __str__(self):
        return self.nombre

# makemigrations = crea el archivo de las migraciones  (el archivo que se envia a la base de datos ej: 0001_initial.py)  
# migrate = envia el archivo a la bd
# createsuperuser = crea el admin de la web
# python -m pip install Pillow para poder subir img y modificar setting.py - urls.py