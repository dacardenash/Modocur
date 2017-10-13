class Usuario:

	def __init__(self, identificador, nombre, apellido, correo, clave, fecha_nacimiento):
		self._identificador = identificador
		self._nombre = nombre
		self._apellido = apellido
		self._correo = correo
		self._clave = clave
		self._fecha_nacimiento = fecha_nacimiento
		self._comentario = []

	def get_identificador(self):
		return self._identificador

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
		existe = Usuario.buscar_por_correo(Usuario.lista_usuarios, correo)
		if(not existe and correo != "Adm@modocur.com"):
			self._correo = correo

	def get_clave(self):
		return self._clave

	def set_clave(self, clave):
		self._clave = clave

	def get_fecha_nacimiento(self):
		return self._fecha_nacimiento

	def set_fecha_nacimiento(self, fecha_de_nacimiento):
		self._fecha_nacimiento = fecha_de_nacimiento

	def get_comentario(self):
		return self._comentario

	def to_string(self):
		return("Usuario{" + "nombre= " + self.get_nombre() + ", apellido= " + self.get_apellido()
			    + ", correo= " + self.get_correo() + ", clave= " + self.get_clave() 
			    + ", fecha_nacimiento= " + self.get_fecha_nacimiento() + '}')

	def login(self, clave):
		if(self.get_clave() == clave):
			return True

	@staticmethod
	def buscar_por_correo(usuarios, correo):
		for usuario in usuarios :
			if(usuario.get_correo() == correo):
				return usuario

	
  
