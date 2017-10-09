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

	def __init__(self):
		self.choices_menu_principal = {
		"1": self.sing_up,
		"2": self.sing_in,
		"3": self.read_txt,
		"4": self.salir,
		"5": self.ingresar_datos_ficticios
		}
		self.choices_menu_estudiante = {
		#"2" : self.inscribirse
		"4" : self.logout
		}
		self.choices_menu_instructor = {
		"1" : self.new_course,
		"14" : self.logout
		}
		self.choices_menu_administrador = {
		"1" : Main.display_estudiantes,
		"2" : Main.display_instructores,
		"3" : Main.display_cursos,
		"4" : self.logout
		}
		self.break_while = True
		self.break_while_sing_in = False

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
	def display_cursos():
		for curso in Main.lista_curso:
			print(curso.to_string())

	def sing_up(self):
		"""
		Crear un nuevo usuario
		"""
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
			usuario = Estudiante(nombre, apellido, correo, clave, fecha_nacimiento) #Desde Estudiante
			Main.lista_estudiante.append(usuario)
			Main.lista_usuarios.append(usuario)
			print(Mensaje.mensaje.get("usuario_created"))
		elif role == 2:
			carrera = input(Mensaje.mensaje.get("input_carer"))
			usuario = Instructor(nombre, apellido, correo, clave, fecha_nacimiento, carrera) #Desde Instructor
			Main.lista_instructor.append(usuario)
			Main.lista_usuarios.append(usuario)
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
		pass

	def salir(self):
		os._exit(0)

	def ingresar_datos_ficticios(self):
		"""Crear Instructor1"""
		instructor1 = Instructor("Juan", "Perez", "Juanpe@instructor.com", "1234", "05-20-1998", "economía")
		Main.lista_instructor.append(instructor1)
		Main.lista_usuarios.append(instructor1)
		"""Crear Estudiante1"""
		estudiante1 = Estudiante("Jorge", "Lopez", "LopezJor@estudiante.com", "1234", "04-07-2005")
		Main.lista_usuarios.append(estudiante1)
		Main.lista_estudiante.append(estudiante1)
		"""Crear Cursos"""
		curso1 = Curso()
		curso1.crear_curso("Economía 1", "Ciencias Económicas", "Primer curso de economía", "01-01-2000", instructor1)
		Main.lista_curso.append(curso1)

		curso2 = Curso()
		curso2.crear_curso("Economía 2", "Ciencias Económicas", "Segundor curso de economía", "01-01-2000", instructor1)
		Main.lista_curso.append(curso2)

	
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

	def new_course(self,instructor):
		"""
		Crear un nuevo curso
		"""
		nombre = input(Mensaje.mensaje.get("input_name"))
		categoria = input(Mensaje.mensaje.get("input_category"))
		descripcion = input(Mensaje.mensaje.get("input_description"))
		fecha_creacion = input(Mensaje.mensaje.get("input_date"))
		curso = Curso() #Desde curso
		curso.crear_curso(nombre, categoria, descripcion, fecha_creacion, instructor)
		Main.lista_curso.append(curso)
		print(Mensaje.mensaje.get("course_created"))
		

		Main.display_cursos()

if __name__ == "__main__":
	Main().run()



  

