class Curso:

	def __init__(self, id, instructor, mensaje, nombre, categoria, estado, fecha_creacion,
				 fecha_finalizacion):
		self._id = id
		self._instructor = instructor
		self._mensaje = mensaje 
		self._nombre = nombre
		self._categoria = categoria
		self._estado = estado
		self._fecha_creacion = fecha_creacion
		self._fecha_finalizacion = fecha_finalizacion
		self._modulos = modulos
		self._inscripcion = []

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