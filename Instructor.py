from Usuario import Usuario

class Instructor(Usuario):

	def __init__(self, nombre, apellido, correo, clave, fecha_nacimiento, carrera):
		super().__init__(nombre, apellido, correo, clave, fecha_nacimiento)
		self._carrera = carrera
		#self._comentarios = []

	def get_carrera(self):
		return self._carrera

	def set_carrera(self, carrera):
		self._carrera = carrera

	#@override
	def to_string(self) :
		return ("Usuario{" + "nombre= " + self.get_nombre() + ", apellido= " + self.get_apellido()
			    + ", correo= " + self.get_correo() + ", fecha_nacimiento= " + self.get_fecha_nacimiento()
			    + ", carrera= " + self.get_carrera() + '}')

