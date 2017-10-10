from Estudiante import Estudiante

class Inscripcion:

	def __init__(self, curso, estudiante):
	    self._curso = curso
	    self._nota = 0
	    self._progreso = 0
	    self._estudiante = estudiante
	    
	@staticmethod	
	def inscribirse (estudiante, curso):
		inscripcion = Inscripcion(curso,estudiante)
		estudiante.get_inscripciones().append(inscripcion)
		curso.get_inscripcion().append(inscripcion)

	def get_curso(self):
		return self._curso

	def get_progreso(self):
		return self._progreso

	def get_nota(self):
		return self._nota

	def to_string(self) :
		return ("Inscripción{" + "curso= " + self.get_curso().get_nombre() + ", progreso= " + str(self.get_progreso())
			    + "%" + "nota= " + str(self.get_nota()) + '}')