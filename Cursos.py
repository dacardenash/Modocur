class Curso:

	lista_curso = []
	cursos_creados  = 0

	def __init__(self, id, nombre, categoria, descripcion, fecha_creacion, instructor):
		self._id = id
		self._nombre = nombre
		self._categoria = categoria
		self._descripcion = descripcion 
		self._fecha_creacion = fecha_creacion
		self._estado = True
		self._instructor = instructor
		instructor._cursos.append(self)
		self._modulos = []
		self._inscripcion = []
		Curso.lista_curso.append(self)
		Curso.cursos_creados += 1

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

	def to_string(self) :
		return ("Curso{" + "id= " + str(self.get_id()) + ", nombre= " + self.get_nombre()
			    + ", categoría= " + self.get_categoria() + ",descripcion= " + self.get_descripcion()
			    + ", fecha_creacion= " + self.get_fecha_creacion() + ", instructor= " 
			    + self.get_instructor().get_nombre() + " " +  self.get_instructor().get_apellido()
			    + '}')


	"""@staticmethod
    def get_curso(id, lista_curso):
    	respuesta=None
    	for reg in lista_curso:
    		if reg.get_id()==id:
    			respuesta=reg
    			return respuesta"""
		
	"""@staticmethod
    def consultar_cursos(lista_curso):
    	respuesta=None
    	for reg in lista_curso:
    		respuesta+=" "+reg.get_id()+"-"+reg.get_nombre()+"/n"

    	return (respuesta)"""

	"""def inscribirse(self):
		Curso.consultar_cursos(lista_curso)
		vble=input("dijite el codigo del curso que desea inscribir:")
		vble2=Curso.get_curso(vble, lista_curso)
		vble3="""