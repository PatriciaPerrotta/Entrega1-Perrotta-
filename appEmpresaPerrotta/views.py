from django.shortcuts import render
from appEmpresaPerrotta.models import Departamento, Empresas_asociadas
from django.http import HttpResponse

from appEmpresaPerrotta.forms import Empresa_formulario
from appEmpresaPerrotta.models import Empleado

# Create your views here.
def departamento_view (request):
    departamento = Departamento.objects.all()
    departamento_lista = list (departamento)
    
    print (departamento_lista)
    
    #return HttpResponse ("<h2>departamentos</h2>") 

    return render(request, "appEmpresaPerrotta/departamento.html",{"departamentos":departamento_lista})


def empresas_asociadas_view (request):
    empresas_asociadas = Empresas_asociadas.objects.all()
    empresas_asociadas_lista = list (empresas_asociadas)
    
    print (empresas_asociadas_lista)
    
    #return HttpResponse ("<h2>empresas_asociadas</h2>") 

    return render(request, "appEmpresaPerrotta/empresas_asociadas.html",{"empresas":empresas_asociadas})

def formulario_empresa_view (request):
    if request.method == "POST": 
        formulario = Empresa_formulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            empresa = Empresas_asociadas(data['nombre'])
            empresa.save()

            formulario = Empresa_formulario()
            return render(request, "appEmpresaPerrotta/formulario_empresa.html", {"formulario":Mi_formulario})

    
    else: 
        
        Mi_formulario= Empresa_formulario ()
        return render (request,"appEmpresaPerrotta/formulario_empresa.html", {"formulario":Mi_formulario})
    

def empleado_view (request):
    empleado = Empleado.objects.all()
    empleado_lista = list (empleado)
    
    print (empleado_lista)
    
    #return HttpResponse ("<h2>empresas_asociadas</h2>") 

    return render(request, "appEmpresaPerrotta/empleado.html",{"empleados":empleado_lista})

#def formulario_empleado_view (request):
    # if request.method == "POST": 
    #     formulario = Empleado_formulario(request.POST)
    #     if formulario.is_valid():
    #         data = formulario.cleaned_data

    #         empleado = Empleado ('nombre', 'apellido', 'email', 'rol'])
    #         empleado.save()

    #         formulario = Empleado_formulario()
    #         return render(request, "appEmpresaPerrotta/formulario_empleado.html", {"formulario":Mi_formulario})

    
    # else: 
        
    #     Mi_formulario= Empleado_formulario ()
    #     return render (request,"appEmpresaPerrotta/formulario_empleado.html", {"formulario":Mi_formulario})
    
    
    

