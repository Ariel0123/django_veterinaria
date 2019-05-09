from django.contrib import admin
from .models import Cirugia, Cita, Cliente, Mascota, RecetaCirugia, RecetaSimple


admin.site.register(Cirugia)
admin.site.register(Cita)
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(RecetaCirugia)
admin.site.register(RecetaSimple)