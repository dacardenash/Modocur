from Usuario import Usuario

class Estudiante(Usuario):

	def __init__(self, identificador, nombre, apellido, correo, clave, fecha_nacimiento):
		super().__init__(identificador, nombre, apellido, correo, clave, fecha_nacimiento)
		self._inscripciones = []

	def get_inscripciones(self):
		return self._inscripciones

	#@override
	def to_string(self) :
		return ("Estudiante{" + "nombre= " + self.get_nombre() + ", apellido= " + self.get_apellido()
			    + ", correo= " + self.get_correo() + ", clave= " + self.get_clave()
			    + ", fecha_nacimiento= " + self.get_fecha_nacimiento() + '}')
