from django import forms


class ProfesionalFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    especialidad = forms.CharField(max_length=60)
    consultorio = forms.IntegerField()

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    obraSocial = forms.CharField(max_length=60)
    historiaClinica = forms.CharField(max_length=60)

class SanatoriosFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    domicilio = forms.CharField(max_length=60)
    telefono = forms.IntegerField()
    
