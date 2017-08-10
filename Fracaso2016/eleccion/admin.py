from django.contrib import admin
from .models import PartidoPolitico, Voto, MesaElectoral, Circunscripcion, Resultado

admin.site.register(PartidoPolitico)
admin.site.register(Voto)
admin.site.register(MesaElectoral)
admin.site.register(Circunscripcion)
admin.site.register(Resultado)
