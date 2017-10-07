class Usuario:

	def __init__(self, nombre, apellido, correo, clave, fecha_nacimiento):

		self._nombre = nombre
		self._apellido = apellido
		self._correo = correo
		self._clave = clave
		self._fecha_nacimiento = fecha_nacimiento

	def get_nombre(self):
		return self._nombre

	def set_nombre(self, nombre):
		self._nombre = nombre

	def get_apellido(self):
		return self._apellido

	def set_apellido(self, apellido):
		self._apellido = apellido

	def get_correo(self):
		return self._correo

	def set_correo(self, correo):
		self._correo = correo

	def get_clave(self):
		return self._clave

	def set_clave(self, clave):
		self._clave = clave

	def get_fecha_de_nacimiento(self):
		return self._fecha_nacimiento

	def set_clave(self, fecha_de_nacimiento):
		self._fecha_nacimiento = fecha_de_nacimiento
