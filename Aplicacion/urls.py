from django.urls import path
from django.urls import include   
from . import views 
from rest_framework.routers import DefaultRouter     

#------------------------------   AGREGADO  -------------------------------
router = DefaultRouter()
router.register(r"productos", views.ProductoViewSet)
router.register(r"cliente", views.ClienteViewSet)
router.register(r"pedido", views.PedidoViewSet)
router.register(r"detalle", views.DetallePedidoViewSet)

urlpatterns = [
    path('categorias/cantidad/', views.producto_count, name='categorias_cantidad'),
    path('', include(router.urls)),    
]