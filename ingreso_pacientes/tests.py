from django.test import TestCase, Client

# Create your tests here.
from ingreso_pacientes.models import Paciente

#Creando casos de prueba
class CrearPaciente(TestCase):
    def setUp(self):
        self.cliente = Client()

    def crear_paciente(self):
        self.paciente = Paciente.objects.create(nombres='Juan',apellidos='Vargas',cedula='0955555555')

    def test_crear_paciente(self):
        self.crear_paciente()
        self.assertIsInstance(self.paciente,Paciente,'paciente creado exitosamente')

    def test_functional_pacientes(self):
        response = self.cliente.get('/pacientes/')
        self.assertEqual(response.status_code,200)

    def test_functional_pacientes_post(self):
        response = self.cliente.post('/pacientes/',{'nombres':'Jhon','apellidos':'Smith','cedula':'9999999999','nro_historia':'111111'})
        self.assertContains(response,'guardado correctamente')
    
    def test_crear_paciente_view(self):
        respuesta = self.cliente.post('/pacientes/',{"nombres":"Jhon","apellidos":"Smith","cedula":"9999999999","nro_historia":"111111"})
        self.assertContains(respuesta,"guardado correctamente")

    # def test_lista_consultas(self):
    #     '''Metodo que prueba que la url /consultas/
    #     responda con estado 200
    #     '''
    #     respuesta = self.cliente.get('/consultas/')
    #     self.assertEqual(respuesta.status_code,200)
