from django.forms import ModelForm, DateField

from ingreso_pacientes.models import Paciente, Consulta, HistoriaClinica


class PacienteForm(ModelForm):
    class Meta:
        model=Paciente
        fields = ['nombres','apellidos','cedula']

class HistoriaClinicaForm(ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['nro_historia']

class ConsultaForm(ModelForm):
    fecha = DateField(input_formats=['%d-%m-%Y',])
    class Meta:
        model = Consulta
        fields = ['fecha','codigo_diagnostico','diagnostico']