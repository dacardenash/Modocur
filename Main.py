import os
from Mensajes import Mensaje
from Instructor import Instructor
from Estudiante import Estudiante
from Usuario import Usuario
from Cursos import Curso
from Comentarios import Comentario
from Inscripciones import Inscripcion

class Main():
	
	lista_curso = []
	lista_instructor = []
	lista_estudiante = []
	lista_usuarios = [Usuario("Diego", "Cardenas", "Adm@modocur.com", "1234", "01-08-2017")]
	lista_inscripcion = []
	lista_modulo = []
	lista_comentario = []

	def __init__(self):
		self.choices_menu_principal = {
			"1": self.sing_up,
			"2": self.sing_in,
			"3": self.read_txt,
			"4": self.salir,
			"5": self.ingresar_datos_ficticios
		}
		self.choices_menu_estudiante = {
			"1" : Main.display_cursos,
			"2" : self.inscription,
			"3" : self.my_courses,
			"4" : self.consultar_modulos,
			"5" : self.comentar_estudiante,
			"6" : self.logout
		}
		self.choices_menu_instructor = {
			"1" : self.new_course,
			"2" : self.modificar_curso,
			"3" : self.consultar_creados,
			"4" : self.comentar_instructor,
			"5" : self.agregar_modulo,
			"6" : self.promedio_progreso,      #de los estudiantes de un curso
			"7" : self.cerrar_curso,
			"8" : self.mayor_promedio,
			"9" : self.curso_mayor,
			"10" : self.generar_reporte,
			"11" : self.porcentaje_ganador,
			"12" : self.modulo_comentado,
			"13" : self.logout
		}
		self.choices_menu_administrador = {
			"1" : Main.display_estudiantes,
			"2" : Main.display_instructores,
			"3" : Main.display_cursos,
			"4" : self.logout
		}
		self.break_while = True
		self.break_while_sing_in = False

#-------------------------------------------------------------------------------------------#

	@staticmethod	
	def display_usuarios():
		registros = ""
		for usuario in Main.lista_usuarios:
			registros +=  usuario.to_string() + "\n"
		return registros

	@staticmethod
	def display_instructores():
		for instructor in Main.lista_instructor:
			print(instructor.to_string())
			for curso in instructor.get_cursos():
				print(curso.to_string())

	@staticmethod		
	def display_estudiantes():
		for estudiante in Main.lista_estudiante:
			print(estudiante.to_string())

	@staticmethod		
	def display_cursos(usuario = None):
		for curso in Main.lista_curso:
			if(curso.getEstado() == True):
				print(curso.to_string())

#-------------------------------------	Menu Principal	---------------------------------------#
	
	def sing_up(self):
		"""
		Registrar un nuevo usuario
		"""
		identificacion = input(Mensaje.mensaje.get("input_identifica"))
		nombre = input(Mensaje.mensaje.get("input_name"))
		apellido = input(Mensaje.mensaje.get("input_lastname"))

		correo = input(Mensaje.mensaje.get("input_mail"))
		usuario = Usuario.buscar_por_correo(Main.lista_usuarios, correo)
		while(usuario):
			print(Mensaje.mensaje.get("mail_exist").format(correo))
			correo = input(Mensaje.mensaje.get("input_mail"))
			usuario = Usuario.buscar_por_correo(Main.lista_usuarios, correo)

		clave = input(Mensaje.mensaje.get("input_key"))
		fecha_nacimiento = input(Mensaje.mensaje.get("input_birth_date"))
		role = int(input(Mensaje.mensaje.get("input_role")))

		if role == 1:
			usuario = Estudiante(identificacion, nombre, apellido, correo, clave, fecha_nacimiento) #Desde Estudiante
			Main.lista_estudiante.append(usuario)
			Main.lista_usuarios.append(usuario)
			print(Mensaje.mensaje.get("usuario_created"))
		elif role == 2:
			carrera = input(Mensaje.mensaje.get("input_carer"))
			usuario = Instructor(identificacion, nombre, apellido, correo, clave, fecha_nacimiento, carrera) #Desde Instructor
			Main.lista_instructor.append(usuario)
			Main.lista_usuarios.append(usuario)


			file = open("FicheroInstructor.txt","w")
			file.write(identificacion + "@@" + nombre + "@@" + apellido + "@@" + correo + "@@" + clave + "@@" + fecha_nacimiento + "@@" + carrera)
			file.close()

			print(Mensaje.mensaje.get("usuario_created"))
		else:
			print(Mensaje.mensaje.get("input_error").format(role))
			
	def sing_in(self):
		"""
		Ingresar a la plataforma
		"""
		ingresar = False
		correo = input(Mensaje.mensaje.get("input_mail"))
		clave = input(Mensaje.mensaje.get("input_key"))
		usuario = Usuario.buscar_por_correo(Main.lista_usuarios, correo)
		if(usuario):								#Verifica que el correo existe
			ingresar = usuario.login(clave)			#Verifica que la clave coincida
			self.break_while_sing_in = True

		if (ingresar and isinstance(usuario, Estudiante)):
			self.run_estudiante(usuario)			#Ingresa al sistema como estudiante
		elif(ingresar and isinstance(usuario, Instructor)):
			self.run_instructor(usuario)			#Ingresa al sistema como instructor
		elif(ingresar and isinstance(usuario, Usuario)):
			self.run_administrador()				#Ingresa al sistema como administrador
		else:
			print(Mensaje.mensaje.get("login_error"))

	def read_txt(self):
		"""LLenar datos instructores"""
		file = open("FicheroInstructor.txt","r")
		for registro in file:
			info = registro.split('@@')
			instruc = Instructor(info[0],info[1],info[2],info[3],info[4],info[5],info[6])
			Main.listar_instructor.append(instruc)

	def salir(self):
		os._exit(0)

	def ingresar_datos_ficticios(self):
		"""Crear Instructor1"""
		instructor1 = Instructor("000100", "Juan", "Perez", "Juanpe@instructor.com", "1234", "05-20-1998", "economía")
		Main.lista_instructor.append(instructor1)
		Main.lista_usuarios.append(instructor1)
		"""Crear Estudiante1"""
		estudiante1 = Estudiante("100100", "Jorge", "Lopez", "LopezJor@estudiante.com", "1234", "04-07-1992")
		Main.lista_usuarios.append(estudiante1)
		Main.lista_estudiante.append(estudiante1)

		estudiante2 = Estudiante("100102", "Maria", "Canela", "maca@gmail.com", "4321", "04-07-1995")
		Main.lista_usuarios.append(estudiante2)
		Main.lista_estudiante.append(estudiante2)

		estudiante3 = Estudiante("100103", "Mauricio", "Duarte", "madu@gmail.com", "0000", "04-07-1996")
		Main.lista_usuarios.append(estudiante3)
		Main.lista_estudiante.append(estudiante3)
		
		"""Crear Cursos"""
		curso1 = Curso("Economía 1", "Ciencias Económicas", "Curso básico en donde se abordan conceptos básicos de economia moderna ", instructor1)
		Main.lista_curso.append(curso1)
		curso2 = Curso("Economía 2", "Ciencias Económicas", "Conceptos macro y micro economicos", instructor1)
		Main.lista_curso.append(curso2)

		"""Crear inscripciones"""
		inscripcion1 = Inscripcion.inscribirse(estudiante1, curso1, lista_inscripcion)
		inscripcion2 = Inscripcion.inscribirse(estudiante2, curso1, lista_inscripcion)
		inscripcion3 = Inscripcion.inscribirse(estudiante3, curso1, lista_inscripcion)
		inscripcion4 = Inscripcion.inscribirse(estudiante2, curso2, lista_inscripcion)

		"""Crear modulos"""
		modulo1 = Modulo.agregar_modulo("¿Qué es economia?", "Ciencia que estudia los recursos, la creación de riqueza y la producción, distribución y consumo de bienes y servicios, para satisfacer las necesidades humanas.", "www.youtube.com/eco", curso1, lista_modulo)
		modulo2 = Modulo.agregar_modulo("Economía teórica", "Busca crear modelos que expliquen los fenómenos económicos.", "www.youtube.com/teo", curso1, lista_modulo)
		modulo3 = Modulo.agregar_modulo("Economía empírica", "Busca la confirmación o refutación de tales modelos mediante experimentación.", "www.youtube.com", curso1, lista_modulo)
		modulo4 = Modulo.agregar_modulo("Microenomía", "Estudio de las elecciones que hacen individuos, empresas y gobiernos", "www.youtube.com/micro", curso2, lista_modulo)
		modulo5 = Modulo.agregar_modulo("Macroeconomía", "Estudio del funcionamiento de la economía nacional y global.", "www.youtube.com/macro", curso2, lista_modulo)
		modulo6 = Modulo.agregar_modulo("Objeto de estudio", "Estudiar la distribución de los bienes económicos.", "www.youtube.com/objeto", curso2, lista_modulo)

		"""crear comentarios""" 
		comentario1 = Comentario.comentar("Muy buena explicación.", estudiante1, modulo1, lista_comentario) 
		comentario2 = Comentario.comentar("No entendi nada.", estudiante2, modulo2, lista_comentario) 
		comentario3 = Comentario.comentar("El contenido es bueno.", estudiante3, modulo2, lista_comentario) 
		comentario4 = Comentario.comentar("Ponganse a estudiar.", instructor1, modulo2, lista_comentario) 


#----------------------------------------------Menú Estudiante-----------------------------------------------#

	def inscription(self, estudiante):
		Main.display_cursos()
		id_curso = int(input(Mensaje.mensaje.get("Id_course")))
		curso = Curso.get_curso(id_curso, Main.lista_curso)
		Inscripcion.inscribirse(estudiante, curso, lista_inscripcion)
		print(Mensaje.mensaje.get("usuario_created"))

	def my_courses(self, estudiante):
		for inscripcion in estudiante.get_inscripciones():
			print(inscripcion.to_string())

	def consultar_modulos(self, estudiante):
		self.my_courses()    
		idcurso = input(Mensaje.mensaje.get("input_cod_curso"))
		obj_curso = Curso.retornar_objeto(idcurso, lista_curso)
		aux_modulos  = obj_curso.get_modulos()
		obj_inscripcion = Inscripcion.retornar_objeto(idcurso, estudiante.get_inscripciones())
		print(Modulo.lista_modulos_acceso(aux_modulos, obj_inscripcion.get_Vistos()))
		idmodulo = input(Mensaje.mensaje.get("input_cod_modulo"))
		print(Modulo.ver_modulo(idmodulo, aux_modulos, obj_inscripcion))

	def comentar_estudiante(self, usuario):
		self.my_courses()
		idcurso = input(Mensaje.mensaje.get("input_cod_curso"))
		print(Modulo.consultar_modulos(idcurso, lista_modulo))
		idmod = input(Mensaje.mensaje.get("input_cod_modulo"))
		modulo = Modulo.retornar_objeto(idmod, lista_modulo)
		descripcion = input(Mensaje.mensaje.get("input_comentar"))
		Modulo.comentar(descripcion, usuario, modulo, lista_comentario)

#---------------------------------------------- Menú Instructor --------------------------------------------#

	def new_course(self,instructor):
		"""
		Crear un nuevo curso
		"""
		nombre = input(Mensaje.mensaje.get("input_name"))
		categoria = input(Mensaje.mensaje.get("input_category"))
		descripcion = input(Mensaje.mensaje.get("input_description"))
		curso = Curso(nombre, categoria, descripcion, instructor) #Desde curso
		Main.lista_curso.append(curso)
		print(Mensaje.mensaje.get("course_created"))
		Main.display_cursos()

	def consultar_creados(self, instructor):
		print(Curso.lista_curso(instructor.get_cursos))

	def comentar_instructor(self, usuario):
		self.consultar_creados(usuario)
		idcurso = input(Mensaje.mensaje.get("input_cod_curso"))
		print(Modulo.consultar_modulos(idcurso, lista_modulo))
		idmod = input(Mensaje.mensaje.get("input_cod_modulo"))
		modulo = Modulo.retornar_objeto(idmod, lista_modulo)
		descripcion = input(Mensaje.mensaje.get("input_comentar"))
		Modulo.comentar(descripcion, usuario, modulo, lista_comentario)

	def agregar_modulo(self, instructor):
		self.consultar_creados(instructor)
		idcurso = input(Mensaje.mensaje.get("input_cod_curso"))
		curso = Curso.retornar_objeto(idcurso, lista_curso)
		titulo = input(Mensaje.mensaje.get("input_titulo_modulo"))
		descripcion = input(Mensaje.mensaje.get("input_descripcion_modulo"))
		url = input(Mensaje.mensaje.get("input_url_modulo"))
		Modulo.agregar_modulo(titulo, descripcion, curso, url, lista_curso)

	def promedio_progreso(self, instructor):
		self.consultar_creados(instructor)
		idcurso = input(Mensaje.mensaje.get("input_cod_curso"))
		curso = Curso.retornar_objeto(idcurso, lista_curso)
		print(Inscripcion.promedio_progreso_general(curso.get_inscripcion()))

	def cerrar_curso(self, instructor):
		self.consultar_creados(instructor)
		idcurso = input(Mensaje.mensaje.get("input_cod_curso"))
		curso = Curso.retornar_objeto(idcurso, lista_curso)
		curso.cerrar_curso()
		Inscripcion.calcular_nota(curso.get_inscripcion)

	def mayor_promedio(self, instructor):
		self.consultar_creados(instructor)
		idcurso = input(Mensaje.mensaje.get("input_cod_curso"))
		curso = Curso.retornar_objeto(idcurso, lista_curso)
		inscripcion_mayor =  Inscripcion.mayor_promedio(curso.get_inscripcion())
		print(inscripcion_mayor)

	def curso_mayor(self, instructor):
		self.consultar_creados(instructor)
		print(Curso.curso_mayor(instructor.get_cursos()))

	def generar_reporte(self, instructor):
		fecha = input(Mensaje.mensaje.get("input_fecha_inicial"))
		print(Curso.generar_reporte(fecha, instructor.get_cursos()))

	def porcentaje_ganador(self, instructor):
		self.consultar_creados(instructor)
		idcurso = input(Mensaje.mensaje.get("input_cod_curso"))
		curso = Curso.retornar_objeto(idcurso, lista_curso)
		print("Porcentaje de aprobados: " + Curso.porcentaje_ganador(curso))

	def modulo_comentado(self, instructor):
		print(Modulo.mayor_comentado(instructor.get_cursos())

#---------------------------------------- Ejecución --------------------------------------------#
	
	def run(self):
		while self.break_while:
			print(Mensaje.mensaje.get("menu_inicio"))
			option = input(Mensaje.mensaje.get("operation"))
			action = self.choices_menu_principal.get(option)
			if action:
				action()
			else:
				print(Mensaje.mensaje.get("input_error").format(option))

	def run_estudiante(self, estudiante):
		while self.break_while_sing_in:
			print (Mensaje.mensaje.get("menu_estudiante"))
			option = input(Mensaje.mensaje.get("operation"))
			action = self.choices_menu_estudiante.get(option)
			if action:
				action(estudiante)
			else:
				print(Mensaje.mensaje.get("input_error").format(option))

	def run_instructor(self, instructor):
		while self.break_while_sing_in:
			print(Mensaje.mensaje.get("menu_instructor"))
			option = input(Mensaje.mensaje.get("operation"))
			action = self.choices_menu_instructor.get(option)
			if action:
				action(instructor)
			else:
				print(Mensaje.mensaje.get("input_error").format(option))

	def run_administrador(self):
		while self.break_while_sing_in:
			print (Mensaje.mensaje.get("menu_administrador"))
			option = input(Mensaje.mensaje.get("operation"))
			action = self.choices_menu_administrador.get(option)
			if action:
				action()
			else:
				print(Mensaje.mensaje.get("input_error").format(option))

	def logout(self, usuario = None):
		self.break_while_sing_in = False
		print(Mensaje.mensaje.get("close_sesion"))

#---------------------------------------------Main---------------------------------------------------#

if __name__ == "__main__":
	Main().run()



  

