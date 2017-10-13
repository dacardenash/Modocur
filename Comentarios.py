import datetime

class Comentario:
	
	def __init__(self, descripcion, usuario, modulo):
		self._fecha = datetime.datetime.today()
		self._descripcion = descripcion
		self._usuario = usuario
		self._modulo = modulo

	def get_fecha(self):
		return self._fecha

	def set_descripcion(self, descripcion):
		self._descripcion =  descripcion 

	def get_descripcion(self):
		return self._descripcion

	def set_usuario(self, usuario):
		self._usuario = usuario

	def get_usuario(self):
		return self._usuario

	def set_modulo(self, modulo):
		self._modulo = modulo

	def get_modulo(self):
		return self._modulo

	@staticmethod
	def comentar(descripcion, usuario, modulo, lista_comenta):
		comentario = Comentario(descripcion, usuario, modulo)
		usuario.get_comentario().append(comentario)
		modulo.get_comentarios().append(comentario)
		lista_comenta.append(comentario)

