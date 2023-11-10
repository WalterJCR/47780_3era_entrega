#Crear un forms.py en el aplicativo y colocar

from django import forms

from Automovil.models import Auto, Conductor, Alquiler

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto # El nombre del model al que se asocia el form
        fields = '__all__' # Para incluir todos los campos del model en el form
        # fields = ['marca', 'modelo', 'color'] # Para incluir solo algunos campos del model en el form
        # exclude = ['placa'] # Para excluir algunos campos del model del form

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = '__all__'

class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = '__all__'