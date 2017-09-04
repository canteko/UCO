from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from apuestas import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='Index'),
	url(r'^login', views.userLogin, name='Login'),
	url(r'^logout', views.userLogout, name='Logout'),
	url(r'^register', views.userRegister, name='Register'),
	url(r'^profile', views.profile, name='Profile'),

	url(r'^apuestas/', include('apuestas.urls', namespace = 'apuestas')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
