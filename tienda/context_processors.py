from home.models import ProductoCategoria

def categorias(request):
    return {'categorias': ProductoCategoria.objects.all()}