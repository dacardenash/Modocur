class Curso:

	lista_curso = []

	def __init__(self, id, nombre, categoria, descripcion, fecha_creacion, instructor):
		self._id = id
		self._nombre = nombre
		self._categoria = categoria
		self._descripcion = descripcion 
		self._fecha_creacion = fecha_creacion
		self._estado = True
		self._instructor = instructor
		self._modulos = []
		self._inscripcion = []
		Curso.lista_curso.append(self)

	def get_id(self):
		return self._id

	def get_nombre(self):
		return self._nombre

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