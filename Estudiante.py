from Usuario import Usuario

class Estudiante(Usuario):

	def __init__(self, nombre, apellido, correo, clave, fecha_nacimiento):
		super().__init__(nombre, apellido, correo, clave, fecha_nacimiento)