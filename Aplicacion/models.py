from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your models here.
def validate_positive(value):
    if value < 0:
        raise ValidationError("El valor debe ser positivo.")
    
def custom_email_validator(value):
    try:
        validate_email(value)
    except ValidationError:
        raise ValidationError('El correo electrónico no es válido.')



class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    mail = models.EmailField(validators=[custom_email_validator])

class Pedido(models.Model):
    fecha_pedido = models.DateField()

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(validators=[validate_positive])