
from .models import Producto, Cliente, Pedido, DetallePedido
from rest_framework import viewsets
from .serializers import ProductoSerializer, ClienteSerializer, PedidoSerializer, DetallePedidoSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

@api_view(["GET"])
def producto_count(request):
    """
    Cantidad de registros en la tabla categorias
    """
    try:
        cantidad = Producto.objects.count()
        return JsonResponse(
            {"cantidad": cantidad},
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, safe=False, status=500)