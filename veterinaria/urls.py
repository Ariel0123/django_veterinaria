from django.urls import path
from .views import (ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView,
    ClienteDeleteView, MascotaListView, MascotaDetailView, MascotaCreateView, MascotaUpdateView,
    MascotaDeleteView, ClienteMascotaListView, CitaListView, CitaDetailView, CitaCreateView,
    CitaUpdateView, CitaDeleteView, MascotaCitaListView, RecetaSimpleListView, RecetaSimpleDetailView,
    RecetaSimpleCreateView, RecetaSimpleUpdateView, RecetaSimpleDeleteView, MascotaRecetaSimpleListView,
    CirugiaListView, CirugiaDetailView, CirugiaCreateView, CirugiaUpdateView, CirugiaDeleteView,
    MascotaCirugiaSimpleListView, RecetaCirugiaListView, RecetaCirugiaDetailView, RecetaCirugiaCreateView,
    RecetaCirugiaUpdateView, RecetaCirugiaDeleteView, CirugiaRecListView, Search
    )

urlpatterns = [

    

    path('cliente/', ClienteListView.as_view(), name='cliente-list'),
    path('cliente/detalle/<int:pk>/', ClienteDetailView.as_view(), name='cliente-id'),
    path('cliente/nuevo/', ClienteCreateView.as_view(), name='cliente-nuevo'),
    path('cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-editar'),
    path('cliente/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente-eliminar'),

    path('busqueda/', Search, name='search'),

    path('cliente/mascota/mascotas/', MascotaListView.as_view(), name='mascota-list'),

    path('cliente/mascota/mascotas/<str:nombre>/', ClienteMascotaListView.as_view(), name='cliente-mascota'),

    path('cliente/mascota/<int:pk>/', MascotaDetailView.as_view(), name='mascota-id'),
    path('cliente/mascota/nuevo/<int:pk>/', MascotaCreateView.as_view(), name='mascota-nuevo'),
    path('cliente/mascota/editar/<int:pk>/', MascotaUpdateView.as_view(), name='mascota-editar'),
    path('cliente/mascota/eliminar/<int:pk>/', MascotaDeleteView.as_view(), name='mascota-eliminar'),

    path('cliente/mascota/cita/', CitaListView.as_view(), name='cita-list'),

    path('cliente/mascota/cita/citas/<str:nombre>/', MascotaCitaListView.as_view(), name='mascota-cita'),

    path('cliente/mascota/cita/<int:pk>/', CitaDetailView.as_view(), name='cita-id'),
    path('cliente/mascota/cita/nuevo/<int:pk>/', CitaCreateView.as_view(), name='cita-nuevo'),
    path('cliente/mascota/cita/editar/<int:pk>/', CitaUpdateView.as_view(), name='cita-editar'),
    path('cliente/mascota/cita/eliminar/<int:pk>/', CitaDeleteView.as_view(), name='cita-eliminar'),

    path('cliente/mascota/receta/recetas/', RecetaSimpleListView.as_view(), name='receta-list'),

    path('cliente/mascota/receta/recetas/<str:nombre>/', MascotaRecetaSimpleListView.as_view(), name='mascota-receta'),

    path('cliente/mascota/receta/<int:pk>/', RecetaSimpleDetailView.as_view(), name='receta-id'),
    path('cliente/mascota/receta/nuevo/<int:pk>/', RecetaSimpleCreateView.as_view(), name='receta-nuevo'),
    path('cliente/mascota/receta/editar/<int:pk>/', RecetaSimpleUpdateView.as_view(), name='receta-editar'),
    path('cliente/mascota/receta/eliminar/<int:pk>/', RecetaSimpleDeleteView.as_view(), name='receta-eliminar'),

    path('cliente/mascota/cirugia/cirugias/', CirugiaListView.as_view(), name='cirugia-list'),

    path('cliente/mascota/cirugia/cirugias/<str:nombre>/', MascotaCirugiaSimpleListView.as_view(), name='mascota-cirugia'),

    path('cliente/mascota/cirugia/<int:pk>/', CirugiaDetailView.as_view(), name='cirugia-id'),
    path('cliente/mascota/cirugia/nuevo/<int:pk>/', CirugiaCreateView.as_view(), name='cirugia-nuevo'),
    path('cliente/mascota/cirugia/editar/<int:pk>/', CirugiaUpdateView.as_view(), name='cirugia-editar'),
    path('cliente/mascota/cirugia/eliminar/<int:pk>/', CirugiaDeleteView.as_view(), name='cirugia-eliminar'),

    path('cliente/mascota/cirugia/receta/recetas/', RecetaCirugiaListView.as_view(), name='recetacirugia-list'),

    path('cliente/mascota/cirugia/receta/recetas/<int:pk>/', CirugiaRecListView.as_view(), name='cirugia-rec'),

    path('cliente/mascota/cirugia/receta/<int:pk>/', RecetaCirugiaDetailView.as_view(), name='recetacirugia-id'),
    path('cliente/mascota/cirugia/receta/nuevo/<int:pk>/', RecetaCirugiaCreateView.as_view(), name='recetacirugia-nuevo'),
    path('cliente/mascota/cirugia/receta/editar/<int:pk>/', RecetaCirugiaUpdateView.as_view(), name='recetacirugia-editar'),
    path('cliente/mascota/cirugia/receta/eliminar/<int:pk>/', RecetaCirugiaDeleteView.as_view(), name='recetacirugia-eliminar'),









    
]