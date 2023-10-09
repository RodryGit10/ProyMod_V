from django.contrib import admin
from .models import Producto, Cliente, Pedido, DetallePedido

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
admin.site.register(Producto, ProductoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mail')
admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Pedido)

class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad')
admin.site.register(DetallePedido, DetallePedidoAdmin)