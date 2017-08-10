from django.contrib import admin
from .models import Destino, Destinatario, Paquete, Ruta

admin.site.register(Destino)
admin.site.register(Destinatario)
admin.site.register(Paquete)
admin.site.register(Ruta)
