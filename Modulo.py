class Modulo:
	
	def __init__(self, ):
		self._id = ""
		self._titulo = ""
		self._descripcion = ""
		self._curso = None
		self._url_video = ""
		self._comentarios = []

	def set_id(self, id):
		self._id = id

	def get_id(self):
		return self._id

	def set_titulo(self, titulo):
		self._titulo = titulo

	def get_titulo(self):
		return self._titulo

	def set_descripcion(self, descripcion):
		self._descripcion = descripcion

	def get_descripcion(self):
		return self._descripcion

	def set_curso(self, curso):
		self._curso = curso

	def get_curso(self):
		return self._curso

	def get_comentarios(self):
		return self._comentarios

	@staticmethod 
	def agregar_modulo(id_modulo, titulo, descripcion, curso, url, lista_modulo):
		modulo = Modulo(id_modulo, titulo, descripcion, curso, url)
		curso.get_modulos().append(modulo)
		lista_modulo.append(modulo)

	@staticmethod
	def consultar_modulos(id_curso, lista_modulo):
		resp = ""
		for modulo in lista_modulo:
			if(modulo.get_curso().get_id() == id_curso):
				resp = resp + "1. " + modulo.get_titulo() + "/n"
		return resp

	@staticmethod
	def ver_modulo(id_modulo, lista_modulo):
		resp = ""
		for modulo in lista_modulo:
			if(modulo.get_id() == id_modulo):
				resp = resp + modulo.get_id() + ". " + modulo.get_titulo() + "/n" + modulo.get_descripcion() + "/n" + modulo.get_url()
		return resp	

	@staticmethod
	def retornar_objeto(id_modulo, lista_modulo):
		resp = None
		for modulo in lista_modulo:
			if(modulo.get_id() == id_modulo):
				resp = modulo
		return resp








