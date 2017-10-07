class Usuario():

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

	def setIdentificador(self, identificador):
		self._identificador = identificador

	def getNombre(self):
		return self._nombre

	def setNombre(self, nombre):
		self._nombre = nombre

	def getApellido(self):
		return self._apellido

	def setApellido(self, apellido):
		self._apellido = apellido

	def getCorreo(self):
		return self._correo

	def setCorreo(self, correo):
		self._correo = correo

	def getClave(self):
		return self._clave

	def setClave(self, clave):
		self._clave = clave

	def getFechaNacimiento(self):
		return self._fecha_nacimiento

	def setFechaNacimiento(self, fechaNacienminto):
		self._fecha_nacimiento = fechaNacienminto

	def guardar_instructor(self, lista, list_usuario):
		lista.append(self)
		list_usuario.append(self)

	def guardar_estudiante(self, lista, list_usuario):
		lista.append(self)
		list_usuario.append(self)

	@staticmethod
	def poblar_instructor(info, lista):
		lista.append(info)


	@staticmethod
	def mostrar_usuarios(lista = None):
		respuesta = ""
		for reg in lista:
			respuesta = respuesta + "id: " + reg.getIdentificador() + ","  
		return respuesta

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
		return resp


