from Usuario import Usuario

class Estudiante(Usuario):


	def __init__(self, nombre, apellido, correo, clave, fecha_nacimiento):
		super().__init__(nombre, apellido, correo, clave, fecha_nacimiento)
		self._comentarios = []


	#@override
	def to_string(self) :
		return ("Usuario{" + "nombre= " + self.get_nombre() + ", apellido= " + self.get_apellido()
			    + ", correo= " + self.get_correo() + ", fecha_nacimiento= " + self.get_fecha_nacimiento()
			    + '}')
