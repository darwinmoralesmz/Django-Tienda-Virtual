from django.urls import path
from .views import *

urlpatterns = [
	path('', home_inicio, name="home_inicio"),

    
    path('contacto/', contacto, name='contacto'),

]