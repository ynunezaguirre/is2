from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from ingreso_pacientes.forms import PacienteForm, HistoriaClinicaForm, ConsultaForm
from ingreso_pacientes.models import HistoriaClinica, Consulta


def listar_crear_paciente(request):
    list = HistoriaClinica.objects.all()
    form = PacienteForm()
    form_h = HistoriaClinicaForm()
    context = {
        'list': list,
        'form': form,
        'form_h':form_h,
    }
    if request.method == 'GET':
        return render(request,'pacientes.tpl.html',context)
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        form_h = HistoriaClinicaForm(request.POST)
        mensaje = 'los campos son incorrectos'
        if form.is_valid() and form_h.is_valid():
            paciente = form.save()
            hist = form_h.instance
            hist.paciente = paciente
            hist.save()
            mensaje = 'guardado correctamente'
        context['mensaje']=mensaje
        return render(request, 'pacientes.tpl.html', context)
    else:
        return HttpResponse('Metodo no disponible',status=404)


def detalles_paciente(request,pk):
    historia = get_object_or_404(HistoriaClinica,pk=pk)
    form = ConsultaForm()
    if request.method=='GET':
        context = {
            'historia':historia,
            'form': form
        }
        return render(request,'detalle_historia.tpl.html',context)
    if request.method=='POST':
        mensaje='consulta no valida'
        form = ConsultaForm(request.POST)
        if form.is_valid():
            detalle = form.instance
            detalle.historia_clinica=historia
            detalle.save()
            mensaje='se guardo correctamente'
        context = {
            'historia': historia,
            'form': form,
            'mensaje':mensaje,
        }
        return render(request,'detalle_historia.tpl.html',context)



# def pacientes_por_diagnosticos(request):
#     """Vista basada en funcion que muestra todas las consultas a la base de
#     datos.
#     """
#     if request.method == 'GET':
#         consultas = Consulta.objects.all()
#         context = {'diagnosticos':consultas}
#         return render(request,'pacientes_por_diagnostico.tpl.html',context)
