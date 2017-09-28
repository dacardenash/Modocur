from Usuario import Usuario

class Instructor(Usuario):

	def __init__(self, identificador, nombre, apellido, correo, clave, fecha_nacimiento, carrera):
		super().__init__(identificador, nombre, apellido, correo, clave, fecha_nacimiento)
		self._carrera = carrera

