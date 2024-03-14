from django.shortcuts import render
from .models import ServicesModel

# Create your views here.
def services(request):
    servicios = ServicesModel.objects.all()
    context = { 'servicios': servicios}
    return render(request, "services/services.html", context)