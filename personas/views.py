from django.shortcuts import render
from personas.models import Persona

# Create your views here.

def tablaPersona(request):
	no_personas = Persona.objects.count()
	return render(request, 'personas.html', {'no_personas': no_personas})
	
def Inicio(request):
	return render(request,'inicio.html')