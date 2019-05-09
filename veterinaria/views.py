from django.shortcuts import render, get_object_or_404
from .models import Cirugia, Cita, Cliente, Mascota, RecetaCirugia, RecetaSimple
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import MascotaForm, CitaForm, CirugiaForm


@login_required
def Search(request):
    query = request.GET.get('q')
    
    items = Cliente.objects.filter(Q(nombre__icontains=query) | Q(primer_apellido__icontains=query) | Q(segundo_apellido__icontains=query))
    items2 = Mascota.objects.filter(Q(nombre__icontains=query))
    

    context = {
        'items': items,
        'items2': items2
       
    }

    return render(request, 'veterinaria/search.html', context)


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'veterinaria/clientes_list.html'
    context_object_name = 'items'

 


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'primer_apellido', 'segundo_apellido', 'telefono', 'correo']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class ClienteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'primer_apellido', 'segundo_apellido', 'telefono', 'correo']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False


class ClienteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cliente
    success_url = '/cliente'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False



#Macotas

#cliente-mascota
class ClienteMascotaListView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'veterinaria/cliente_mascota.html'
    context_object_name = 'items'

    def get_queryset(self):
        dueno = get_object_or_404(Cliente, nombre=self.kwargs.get('nombre'))
        return Mascota.objects.filter(dueno=dueno)


class MascotaListView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'veterinaria/mascotas_list.html'
    context_object_name = 'items'


class MascotaDetailView(LoginRequiredMixin, DetailView):
    model = Mascota


class MascotaCreateView(LoginRequiredMixin, CreateView):
    model = Mascota
    form_class = MascotaForm

    def form_valid(self, form):
        form.instance.dueno = Cliente.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)


class MascotaUpdateView(LoginRequiredMixin, UpdateView):
    model = Mascota
    form_class = MascotaForm


class MascotaDeleteView(LoginRequiredMixin,  DeleteView):
    model = Mascota
    success_url = '/cliente'



#citas
class MascotaCitaListView(LoginRequiredMixin, ListView):
    model = Cita
    template_name = 'veterinaria/mascota_cita.html'
    context_object_name = 'items'

    def get_queryset(self):
        mascota = get_object_or_404(Mascota, nombre=self.kwargs.get('nombre'))
        return Cita.objects.filter(mascota=mascota)


class CitaListView(LoginRequiredMixin, ListView):
    model = Cita
    template_name = 'veterinaria/citas_list.html'
    context_object_name = 'items'


class CitaDetailView(LoginRequiredMixin, DetailView):
    model = Cita


class CitaCreateView(LoginRequiredMixin, CreateView):
    model = Cita
    form_class = CitaForm

    def form_valid(self, form):
        form.instance.mascota = Mascota.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)


class CitaUpdateView(LoginRequiredMixin, UpdateView):
    model = Cita
    form_class = CitaForm

class CitaDeleteView(LoginRequiredMixin, DeleteView):
    model = Cita
    success_url = '/cliente'


#recetas simples
class MascotaRecetaSimpleListView(LoginRequiredMixin, ListView):
    model = RecetaSimple
    template_name = 'veterinaria/mascota_receta.html'
    context_object_name = 'items'

    def get_queryset(self):
        mascota = get_object_or_404(Mascota, nombre=self.kwargs.get('nombre'))
        return RecetaSimple.objects.filter(mascota=mascota)


class RecetaSimpleListView(LoginRequiredMixin, ListView):
    model = RecetaSimple
    template_name = 'veterinaria/recetas_list.html'
    context_object_name = 'items'


class RecetaSimpleDetailView(LoginRequiredMixin, DetailView):
    model = RecetaSimple


class RecetaSimpleCreateView(LoginRequiredMixin, CreateView):
    model = RecetaSimple
    fields = ['expediente', 'receta', 'nota']

    def form_valid(self, form):
        form.instance.mascota = Mascota.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)


class RecetaSimpleUpdateView(LoginRequiredMixin, UpdateView):
    model = RecetaSimple
    fields = ['expediente', 'receta', 'nota']

class RecetaSimpleDeleteView(LoginRequiredMixin, DeleteView):
    model = RecetaSimple
    success_url = '/cliente'



#cirugias
class MascotaCirugiaSimpleListView(LoginRequiredMixin, ListView):
    model = Cirugia
    template_name = 'veterinaria/mascota_cirugia.html'
    context_object_name = 'items'

    def get_queryset(self):
        mascota = get_object_or_404(Mascota, nombre=self.kwargs.get('nombre'))
        return Cirugia.objects.filter(mascota=mascota)


class CirugiaListView(LoginRequiredMixin, ListView):
    model = Cirugia
    template_name = 'veterinaria/cirugias_list.html'
    context_object_name = 'items'


class CirugiaDetailView(LoginRequiredMixin, DetailView):
    model = Cirugia


class CirugiaCreateView(LoginRequiredMixin, CreateView):
    model = Cirugia
    form_class = CirugiaForm

    def form_valid(self, form):
        form.instance.mascota = Mascota.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)


class CirugiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Cirugia
    form_class = CirugiaForm

class CirugiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Cirugia
    success_url = '/cliente'



#recetas cirugias
class CirugiaRecListView(LoginRequiredMixin, ListView):
    model = RecetaCirugia
    template_name = 'veterinaria/cirugia_recetacirugia.html'
    context_object_name = 'items'

    def get_queryset(self):
        cirugia = get_object_or_404(Cirugia, id=self.kwargs.get('pk'))
        return RecetaCirugia.objects.filter(cirugia=cirugia)


class RecetaCirugiaListView(LoginRequiredMixin, ListView):
    model = RecetaCirugia
    template_name = 'veterinaria/recetacirugia_list.html'
    context_object_name = 'items'


class RecetaCirugiaDetailView(LoginRequiredMixin, DetailView):
    model = RecetaCirugia

class RecetaCirugiaCreateView(LoginRequiredMixin, CreateView):
    model = RecetaCirugia
    fields = ['receta', 'expediente', 'nota']

    def form_valid(self, form):
        form.instance.cirugia = Cirugia.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)


class RecetaCirugiaUpdateView(LoginRequiredMixin, UpdateView):
    model = RecetaCirugia
    fields = ['receta', 'expediente', 'nota']

class RecetaCirugiaDeleteView(LoginRequiredMixin, DeleteView):
    model = RecetaCirugia
    success_url = '/cliente'



