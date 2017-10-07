
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

	def get_fecha_nacimiento(self):
		return self._fecha_nacimiento

	def set_fecha_nacimiento(self, fecha_de_nacimiento):
		self._fecha_nacimiento = fecha_de_nacimiento

	def to_string(self) :
		return ("Usuario{" + "nombre= " + self.get_nombre() + ", apellido= " + self.get_apellido()
			    + ", correo= " + self.get_correo() + ", fecha_nacimiento= " + self.get_fecha_nacimiento()
			    + '}')

	@staticmethod
	def buscar_por_correo(usuarios, correo):
		for usuario in usuarios :
			if(usuario.get_correo() == correo):
				return usuario
    
"""
	@staticmethod
	def loguear(correo, clave, lista_instruc, lista_estudiante):
		resp = 0
		for reg in lista_instruc:
			#print(reg.getCorreo() + " " + correo + " " + reg.getClave() + " " + clave)
			if(reg.getCorreo() == correo and reg.getClave() == clave):
				resp = 1

		for reg in lista_estudiante:
			if(reg.getCorreo() == correo and reg.getClave() == clave):
				resp = 2
		return resp"""
