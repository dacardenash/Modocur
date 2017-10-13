import datetime
from inscripciones import Inscripcion

class Curso:

	cursos_creados  = 1000

	def __init__(self, nombre, categoria, descripcion, instructor):
		Curso.cursos_creados += 1
		self._id = Curso.cursos_creados
		self._nombre = nombre
		self._categoria = categoria
		self._descripcion = descripcion
		self._fecha_creacion = datetime.date.Today()
		self._estado = True
		self._instructor = instructor
		self._modulos = []
		self._inscripcion = []
		instructor.set_cursos(self)

	def get_modulos(self):
		return self._modulos

	def get_inscripcion(self):
		return self._inscripcion
		
	def get_id(self):
		return self._id

	def set_id(self, iden):
		self._id = iden

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

	def cerrar_curso(self):
		self.set_estado(False)

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
	
	@staticmethod
	def lista_cursos(lista_curso):
		resp = ""
		for curso in lista_curso:
			resp = resp + curso.get_id() + ". " + curso.get_nombre() + "/n"
		return resp

	@staticmethod
	def retornar_objeto(id_curso,lista):
		res = None
		for reg in lista:
			if(reg.get_id() == id_curso):
				res = reg
		return res

	@staticmethod
	def curso_mayor(lista_curso):
		con = 0
		obj = None
		for curso in lista_curso:
			if(con > curso.get_inscripcion().lenght()):
				con = curso.get_inscripcion().lenght()
				obj = curso
		return "Codigo: " + str(obj.get_id()) + "| Nombre: " + str(obj.get_nombre()) + "| N° estudiantes: " + str(obj.get_inscripcion().lenght())

	@staticmethod
	def generar_reporte(fecha, lista):
		res = ""
		for curso in lista:
			if(curso.get_fecha_creacion() >= fecha):
				res = res + " Fecha creacion: " + curso.get_fecha_creacion() + " | Nombre: " + 
					curso.get_nombre() + " | N° inscripciones:" + curso.get_inscripcion().lenght() + 
					" | Promedio: " + Inscripcion.promedio_nota_general(curso.get_inscripcion()) + "/n"
		return res

	@staticmethod
	def porcentaje_ganador(curso):
		inscripciones = curso.get_inscripcion()
		acu = 0
		for inscripc in inscripciones:
			if(inscrip.get_Nota() >= 3):
				acu = acu + 1
		return ("%.1f" % ((acu * 100) / inscripciones.lenght()))

