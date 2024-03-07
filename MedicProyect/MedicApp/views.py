from django.shortcuts import render
from django.http import HttpResponse
from MedicApp.models import Profesional, Paciente, Sanatorios
from MedicApp.forms import ProfesionalFormulario, PacienteFormulario, SanatoriosFormulario

def inicio(request):
    return render(request, "MedicApp/inicio.html")

def profesional(request):
    if request.method == "POST":
        formulario = ProfesionalFormulario(request.POST)
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            alta_profesionales = Profesional(nombre = info_dict["nombre"],
                                           especialidad = info_dict["especialidad"],
                                           consultorio = info_dict["consultorio"])
            alta_profesionales.save()
            return render(request, "MedicApp/alta_exitosa.html")
    else:
        formulario = ProfesionalFormulario()
    return render(request, "MedicApp/alta_profesionales.html", {"form":formulario})


def paciente(request):
    if request.method == "POST":
        formulario = PacienteFormulario(request.POST)
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            alta_pacientes = Paciente(nombre = info_dict["nombre"],
                                           obraSocial = info_dict["obraSocial"],
                                           historiaClinica = info_dict["historiaClinica"])
            alta_pacientes.save()
            return render(request, "MedicApp/alta_exitosa.html")
    else:
        formulario = PacienteFormulario()
    return render(request, "MedicApp/alta_pacientes.html", {"form":formulario})


def sanatorio(request):
    if request.method == "POST":
        formulario = SanatoriosFormulario(request.POST)
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            alta_sanatorios = Sanatorios(nombre = info_dict["nombre"],
                                           domicilio = info_dict["domicilio"],
                                           telefono = info_dict["telefono"])
            alta_sanatorios.save()
            return render(request, "MedicApp/alta_exitosa.html")
    else:
        formulario = SanatoriosFormulario()
    return render(request, "MedicApp/alta_sanatorios.html", {"form":formulario})


def buscar_profesional(request):
    return render(request, "MedicApp/buscar_profesional.html")

def resultado_profesional(request):
    profesional = request.GET["nombre_profesional"]
    resultados = Profesional.objects.filter(nombre__iexact=profesional)
    return render(request, "medicApp/resultados.html", {"resultados":resultados})

