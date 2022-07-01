from django.urls import path, include
from .views import index, contacto,  tienda, agregar_producto, listar_productos,modificar_producto, eliminar_producto, ProductoViewset
from rest_framework import routers
router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
    path('tienda/', tienda, name='tienda'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-productos/', listar_productos, name='listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('api/', include(router.urls)),
]