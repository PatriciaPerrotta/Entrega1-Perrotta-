from django import forms

class Empresa_formulario (forms.Form):
    nombre=forms.CharField (max_length=50)
    
    