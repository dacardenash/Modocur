from Usuario import Usuario

class Estudiante(Usuario):

	def __init__(self, identificador, nombre, apellido, correo, clave, fecha_nacimiento):
		super().__init__(identificador, nombre, apellido, correo, clave, fecha_nacimiento)