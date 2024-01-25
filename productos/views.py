from django.shortcuts import render
from home.models import *
from django.http import Http404
from utilidades import utilidades
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def productos_detalle(request, id, slug):
    try:
        datos=Producto.objects.filter(pk=id).filter(slug=slug).filter(estado_id=1).get()
    except Producto.DoesNotExist:
        raise Http404
    relacionados=Producto.objects.filter(estado_id=1, producto_categoria=datos.producto_categoria_id).filter(estado_id=1).all()[:8]
    fotos=ProductoFotos.objects.filter(producto_id=id).all()
    return render(request, 'productos/detalle.html', {'datos':datos, 'relacionados': relacionados, 'fotos': fotos})



def detalle_categoria(request, id):
    try:
        datos = ProductoCategoria.objects.filter(pk=id).get()
        datos1 = Producto.objects.filter(producto_categoria_id=id).filter(estado_id=1).all()
    except ProductoCategoria.DoesNotExist:
        raise Http404("La categoría de producto no existe")

    # Número de productos a mostrar por página
    productos_por_pagina = 16
    
    # Crear un objeto Paginator para los productos
    paginator = Paginator(datos1, productos_por_pagina)

    # Obtener el número de página desde la solicitud GET
    page = request.GET.get('page')

    try:
        # Obtener la página actual
        productos_pagina = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un entero, mostrar la primera página
        productos_pagina = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, mostrar la última página
        productos_pagina = paginator.page(paginator.num_pages)

    return render(request, 'productos/categoria.html', {'datos': datos, 'productos_pagina': productos_pagina})


def todos_productos(request):
    datos=Producto.objects.filter(estado_id=1).all()
    return render(request, 'productos/productos.html', {'datos':datos})
# falta views

def buscar_productos(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        resultados = Producto.objects.filter(nombre__icontains=query, estado_id=1)

    return render(request, 'productos/busqueda.html', {'query': query, 'resultados': resultados})