from Usuario import Usuario
from Cursos import Curso

class Instructor(Usuario):

	lista_instructor = []

	def __init__(self, nombre, apellido, correo, clave, fecha_nacimiento, carrera):
		super().__init__(nombre, apellido, correo, clave, fecha_nacimiento)
		self._carrera = carrera
		self._cursos = []
		self._comentarios = []
		Instructor.lista_instructor.append(self)
		
	def get_carrera(self):
		return self._carrera

	def set_carrera(self, carrera):
		self._carrera = carrera

	def get_cursos(self):
		return self._cursos



	#@override
	def to_string(self) :
		return ("Instructor{" + "nombre= " + self.get_nombre() + ", apellido= " + self.get_apellido()
			    + ", correo= " + self.get_correo() + ",clave= " + self.get_clave()
			    + ", fecha_nacimiento= " + self.get_fecha_nacimiento()
			    + ", carrera= " + self.get_carrera() + '}')

