from django.urls import path


from appEmpresaPerrotta.views import departamento_view, empresas_asociadas_view, formulario_empresa_view, empleado_view


urlpatterns = [
    path ("/departamento/", departamento_view ),
    path ("/empresas/", empresas_asociadas_view ),
    path ("/empleado/", empleado_view ),
    path ("/formularioEmpresa/", formulario_empresa_view ),

]

