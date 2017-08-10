from django.conf.urls import patterns, include, url
from entregas import views
from .views import *

urlpatterns = patterns ('',

	#Destinatarios
	url (r'^verDestinatario', views.verDestinatario, name='Ver Destinatarios'),
	url (r'^detalleDestinatario/(?P<destinatario_id>\d+)', views.detalleDestinatario, name='Detalles Destinatario'),
	url (r'^addDestinatario', views.addDestinatario, name='Anadir Destinatario'),

	#Destinos
	url (r'^verDestino', views.verDestino, name='Ver Destinos'),
	url (r'^detalleDestino/(?P<destino_id>\d+)', views.detalleDestino, name='Detalles Destino'),
	url (r'^addDestino', views.addDestino, name='Anadir Destino'),

	#Paquetes
	url (r'^verPaquete', views.verPaquete, name='Ver Paquetes'),
	url (r'^addPaquete', views.addPaquete, name='Anadir Paquete'),
	url (r'^detallePaquete/(?P<paquete_id>\d+)', views.detallePaquete, name='Detalles de Paquete'),

	#Rutas (con Vistas basadas en clases)
	url (r'^verRuta', verRuta.as_view(), name='Ver Ruta'),
	url (r'^addRuta', addRuta.as_view(), name='Anadir Ruta'),
	url (r'^detalleRuta/(?P<Ruta_id>\w+)$', detalleRuta.as_view(), name='Detalles Ruta'),

)
