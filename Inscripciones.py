#from Estudiante import Estudiante
import datetime

class Inscripcion:

	#def __init__(self, curso, estudiante):
	def __init__(self, estudiante = None, curso = None):
	    self._fecha = datetime.date.today()
	    self._nota = 0
	    self._num_vistos = 0
	    self._progreso = 0
	    self._estudiante = estudiante   #objeto estudiante
	    self._curso = curso

	def get_Fecha(self):
		return self._fecha

	def set_Nota(self, nota):
		self._nota = nota

	def get_Nota(self):
		return self._nota

	def set_Vistos(self, numero):
		self._num_vistos = numero

	def get_Vistos(self):
		return self._num_vistos

	def set_Progreso(self, progreso):
		self._progreso = progreso

	def get_Progreso(self):
		return self._progreso

	def set_estudiante(self, estudiante):
		self._estudiante = estudiante

	def get_estudiante(self):
		return self._estudiante

	def set_curso(self, curso):
		self._curso = curso

	def get_curso(self):
		return self._curso 
	    
	@staticmethod	
	def inscribirse (estudiante, curso, lista_inscripcion):
		inscripcion = Inscripcion(estudiante, curso) 
		estudiante.get_inscripciones().append(inscripcion)
		curso.get_inscripcion().append(inscripcion)
		lista_inscripcion.append(inscripcion)

	def calcular_progreso(self):
		pass

	def to_string(self) :
		return ("Inscripción{" + "curso= " + self.get_curso().get_nombre() + ", progreso= " + str(self.get_progreso())
			    + "%" + "nota= " + str(self.get_nota()) + '}')