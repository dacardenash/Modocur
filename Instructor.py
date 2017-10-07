from Usuario import Usuario

class Instructor(Usuario):

	lista_instructor = []

	def __init__(self, nombre, apellido, correo, clave, fecha_nacimiento, carrera):
		super().__init__(nombre, apellido, correo, clave, fecha_nacimiento)
		self._carrera = carrera
		Instructor.lista_instructor.append(self)

