class Curso:

	lista_curso = []
	cursos_creados  = 0

	def __init__(self):
		self._id = 0
		self._nombre = ""
		self._categoria = ""
		self._descripcion = ""
		self._fecha_creacion = ""
		self._estado = True
		self._instructor = None
		self._modulos = []
		self._inscripcion = []

	def get_inscripcion(self):
		return self._inscripcion
		
	def get_id(self):
		return self._id

	def set_id(self, id):
		self._id = id

	def get_nombre(self):
		return self._nombre

	def set_nombre(self, nombre):
		self._nombre = nombre

	def get_categoria(self):
		return self._categoria

	def set_categoria(self, categoria):
		self._categoria = categoria

	def get_descripcion(self):
		return self._descripcion

	def set_descripcion(self, descripcion):
		self._descripcion = descripcion

	def get_fecha_creacion(self):
		return self._fecha_creacion

	def set_fecha_creacion(self, fecha_creacion):
		self._fecha_creacion = fecha_creacion

	def get_estado(self):
		return self._estado

	def set_estado(self, estado):
		self._estado = estado

	def get_instructor(self):
		return self._instructor

	def set_instructor(self, instructor):
		self._instructor = instructor

	def crear_curso(self, nombre, categoria, descripcion, fecha_creacion, instructor):
		Curso.cursos_creados += 1
		self.set_id(Curso.cursos_creados)
		self.set_nombre(nombre)
		self.set_categoria(categoria)
		self.set_descripcion(descripcion)
		self.set_fecha_creacion(fecha_creacion)
		self.set_instructor(instructor)
		instructor._cursos.append(self)
		Curso.lista_curso.append(self)



	def to_string(self) :
		return ("Curso{" + "id= " + str(self.get_id()) + ", nombre= " + self.get_nombre()
			    + ", categoría= " + self.get_categoria() + ",descripcion= " + self.get_descripcion()
			    + ", fecha_creacion= " + self.get_fecha_creacion() + ", instructor= " 
			    + self.get_instructor().get_nombre() + " " +  self.get_instructor().get_apellido()
			    + '}')
		
	@staticmethod
	def get_curso(id, lista_curso):
		for curso in lista_curso:
			if curso.get_id()==id:
				return curso
		
	"""@staticmethod
    def consultar_cursos(lista_curso):
    	respuesta=None
    	for reg in lista_curso:
    		respuesta+=" "+reg.get_id()+"-"+reg.get_nombre()+"/n"

    	return (respuesta)"""

