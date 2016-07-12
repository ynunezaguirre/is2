from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombres = models.CharField(max_length=500)
    apellidos = models.CharField(max_length=500)
    cedula = models.CharField(max_length=10)

    def __unicode__(self):
        return '%s %s'%(self.apellidos,self.nombres)

class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(Paciente)
    nro_historia= models.CharField(max_length=6)


class Consulta(models.Model):
    historia_clinica = models.ForeignKey(HistoriaClinica,related_name='consultas')
    fecha = models.DateField()
    diagnostico = models.CharField(max_length=500)
    codigo_diagnostico = models.CharField(unique=True,max_length=10)