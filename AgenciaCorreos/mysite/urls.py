from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
# from mysite import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	# url(r'^$', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # url(r'^AgenciaViajes/', include('AgenciaViajes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url (r'^login', views.userLogin, name='Login'),
    # url (r'^logout', views.userLogout, name='Logout'),
	url(r'^entregas/', include ('entregas.urls', namespace = 'entregas')),
]
