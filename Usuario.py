class Usuario:

	list_usuarios= []

	def __init__(self, identificador, nombre, apellido, correo, clave, fecha_nacimiento):
		self._identificador = identificador
		self._nombre = nombre
		self._apellido = apellido
		self._correo = correo
		self._clave = clave
		self._fecha_nacimiento = fecha_nacimiento
		#self._comentarios = comentarios                   #Aqui falta integrarlo con la clase comentarios


	def getIdentificador(self):
		return self._identificador

	def guardar(self):
		list_usuarios.append(self)

	@staticmethod
	def poblar_usuario(info):
		Usuario.list_usuarios.append(info)

	@staticmethod
	def mostrar_usuarios():
		respuesta = ""
		for reg in Usuario.list_usuarios:
			respuesta = respuesta + "id: " + reg.getIdentificador() + "," 
		return respuesta


