from django.shortcuts import render
from home.models import *


def home_inicio(request):
	datos=Producto.objects.filter(estado_id=1).order_by('-id').all()[:12]
	fechas = Producto.objects.filter(estado_id=1).order_by('-fecha').all()[:12]
	stoks = Producto.objects.filter(estado_id=1).order_by('-stock').all()[:12]
	return render(request, 'home/home.html', {'datos':datos, 'fechas':fechas,'stoks':stoks,}
        )



def contacto(request):
    return render(request, 'home/contacto.html')