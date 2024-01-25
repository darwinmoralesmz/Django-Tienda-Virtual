from django.urls import path
from .views import *

urlpatterns = [
	path('detalle/<int:id>/<str:slug>', productos_detalle, name="productos_detalle"),
	path('categoria/<int:id>', detalle_categoria, name="detalle_categoria"),
	path('todos', todos_productos, name="todos_productos"),
    path('buscar/', buscar_productos, name='buscar_productos'),

]