# taxi/views.py (Substitua o conteúdo inteiro por este)
from django.views.generic import ListView
from .models import Driver, Car, Manufacturer # Importe todos os modelos

# ... (outras views que você já tem)

class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "drivers" # Seu nome de contexto atual

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get("q")
        if search_term:
            queryset = queryset.filter(username__icontains=search_term)
        return queryset


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "cars" # Assumindo 'cars' como contexto para carros

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get("q")
        if search_term:
            queryset = queryset.filter(model__icontains=search_term)
        return queryset


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturers" # Assumindo 'manufacturers' como contexto para fabricantes

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get("q")
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset

# ... (resto do arquivo)