from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test_template/$', views.test_template, name='test_template'),
   url(r'^crear_restaurante/$', views.crear_restaurante, name='crear_restaurante'),
  url(r'^buscar_restaurante/$', views.buscar_restaurante, name='buscar_restaurante'),
  url(r'^info/$',views.info, name='info'),
  url(r'^highcarts/$',views.highcarts, name='highcarts'),
  url(r'^buscar_restaurantesajax/$', views.buscar_restaurantesajax, name='buscar_restaurantesajax'),
  url(r'^modificar_restaurantes/$', views.modificar_restaurantesG, name='modificar_restaurantesG'),
  url(r'^modificar_restaurantes/(?P<id>[0-9]+)/', views.modificar_restaurantes,name='modificar_restaurantes'),
  url(r'^info/(?P<coord>[0-9]+)/', views.info, name='info-detail'),
  
]
