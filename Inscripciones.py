#from Estudiante import Estudiante
import datetime

class Inscripcion:

	def __init__(self, estudiante, curso):
	    self._fecha = datetime.date.today()
	    self._nota = 0
	    self._num_vistos = 0
	    self._progreso = 0
	    self._estudiante = estudiante   
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
	def mayor_promedio(lista_inscripcion):
		aux = 0
		res = None
		for inscri in lista_inscripcion:
			if(aux <= inscri.get_Nota()):
				aux = inscri.get_Nota()
				res = inscri
		return res.get_estudiante().get_nombre() + " " + res.get_estudiante().get_apellido() + " Nota: " + res.get_Nota() + "/n"


	@staticmethod
	def calcular_nota(lista_inscripciones):
		for inscrip in lista_inscripciones:
			inscrip.set_nota((5 * inscrip.get_Progreso())/100)

	@staticmethod
	def promedio_progreso_general(lista_inscripciones):
		acu = 0
		for inscrip in lista_inscripciones:
			acu = acu + inscrip.get_Progreso()
		return ("%.1f" % (acu / (lista_inscripciones.lenght())))

	@staticmethod
	def promedio_nota_general(lista_inscripciones):
		acu = 0
		for inscrip in lista_inscripciones:
			acu = acu + inscrip.get_Nota()
		return ("%.1f" % (acu / (lista_inscripciones.lenght())))

	@staticmethod	
	def inscribirse (estudiante, curso, lista_inscripcion):
		inscripcion = Inscripcion(estudiante, curso) 
		estudiante.get_inscripciones().append(inscripcion)
		curso.get_inscripcion().append(inscripcion)
		lista_inscripcion.append(inscripcion)

	@staticmethod
	#retorna un objeto inscripcion de acuerdo al id del curso
	def retornar_objeto(id_curso, lista_inscripcion):
		res = None
		for inscri in lista_inscripcion:
			if(inscri.get_curso().get_id() == id_curso):
				res = inscri
		return res

	def calcular_progreso(self, total_modulos):
		pro = (self.get_Vistos() * 100) / total_modulos
		self.set_Progreso("%.1f" % pro)		

	def to_string(self) :
		return ("Inscripción{" + "curso= " + self.get_curso().get_nombre() + ", progreso= " + str(self.get_progreso())
			    + "%" + "nota= " + str(self.get_nota()) + '}')