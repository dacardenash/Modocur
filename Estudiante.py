from Usuario import Usuario

class Estudiante(Usuario):

	lista_estudiante = []

	def __init__(self, nombre, apellido, correo, clave, fecha_nacimiento):
		super().__init__(nombre, apellido, correo, clave, fecha_nacimiento)
		Estudiante.lista_estudiante.append(self)