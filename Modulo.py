class Modulo:
	
	identi =  100

	def __init__(self, titulo, descripcion, url, curso):
		Modulo.identi += 1
		self._id = Modulo.identi
		self._titulo = titulo
		self._descripcion = descripcion
		self._curso = curso
		self._url_video = url
		self._comentarios = []

	def set_id(self, iden):
		self._id = iden

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
	def agregar_modulo(titulo, descripcion, url, curso, lista_modulo):
		modulo = Modulo(titulo, descripcion, url, curso)
		curso.get_modulos().append(modulo)
		lista_modulo.append(modulo)

	@staticmethod
	def lista_modulos_acceso(lista_modulos, numero_vistos):
		res = ""
		numero_vistos = numero_vistos + 1
		for num, mod in enumerate(lista_modulos):
			if(num <= numero_vistos):
				res =  res + modulo.get_id() + ". " + modulo.get_titulo() + " Disponible" + "/n"
			else:
				res =  res + modulo.get_id() + ". " + modulo.get_titulo() + " Bloqueado" + "/n"
		return res

	@staticmethod
	def consultar_modulos(id_curso, lista_modulo):
		resp = ""
		for modulo in lista_modulo:
			if(modulo.get_curso().get_id() == id_curso):
				resp = resp + "1. " + modulo.get_titulo() + "/n"
		return resp

	@staticmethod
	def ver_modulo(id_modulo, lista_modulo, inscripcion):
		resp = ""
		for modulo in lista_modulo:
			if(modulo.get_id() == id_modulo):
				resp = resp + modulo.get_id() + ". " + modulo.get_titulo() + "/n" + modulo.get_descripcion() + "/n" + modulo.get_url()
				inscripcion.set_Vistos(inscripcion.get_vistos() + 1)
				inscripcion.calcular_progreso(lista_modulo.length())
		return resp

	@staticmethod
	def retornar_objeto(id_modulo, lista_modulo):
		resp = None
		for modulo in lista_modulo:
			if(modulo.get_id() == id_modulo):
				resp = modulo
		return resp

	@staticmethod
	def mayor_comentado(lista_cursos):
		resp = ""
		obj = None
		num_comentarios = 0
		for curso in lista_cursos:
			for modulo in curso.get_modulos():
				if(modulo.get_comentarios().lenght() > num_comentarios):
					obj = modulo
		return  "curso: " + obj.get_curso().get_id() + " - " obj.get_curso().get_nombre() obj.get_titulo + " | Modulo: " + obj.get_titulo()






