from Usuario import Usuario

class Estudiante(Usuario):

	lista_estudiante = []

	def __init__(self, nombre, apellido, correo, clave, fecha_nacimiento):
		super().__init__(nombre, apellido, correo, clave, fecha_nacimiento)
		Estudiante.lista_estudiante.append(self)
		self._comentarios = []
		self._inscripciones = []

	def get_inscripciones(self):
		return self._inscripciones

	#@override
	def to_string(self) :
		return ("Estudiante{" + "nombre= " + self.get_nombre() + ", apellido= " + self.get_apellido()
			    + ", correo= " + self.get_correo() + ", clave= " + self.get_clave()
			    + ", fecha_nacimiento= " + self.get_fecha_nacimiento() + '}')
