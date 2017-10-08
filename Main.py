import sys
from Mensajes import Mensajes
from Instructor import Instructor
from Estudiante import Estudiante
from Usuario import Usuario

class Main():

	lista_instructor = []
	lista_estudiante = []
	lista_usuarios = []

	def __init__(self):
		self.choices_menu_principal = {
		"1": self.sing_up,
		"2": self.sing_in,
		"3": self.read_txt,
		"4": self.salir,
		"5": self.ingresar_datos_ficticios
		}
		self.break_while = True

	@staticmethod	
	def display_usuarios():
		for usuario in Main.lista_usuarios:
			print(usuario.to_string())

	@staticmethod
	def display_instructores():
		for instructor in Main.lista_instructor:
			print(instructor.to_string())

	@staticmethod		
	def display_estudiantes():
		for estudiante in Main.lista_estudiante:
			print(estudiante.to_string())

	@staticmethod	
	def display_menu_inicio():
		print(Mensajes.mensaje.get("menu_inicio"))

	@staticmethod
	def display_menu_instructor():
		print(Mensajes.mensaje.get("menu_instructor"))

	@staticmethod
	def display_menu_estudiante():
		print (Mensajes.mensaje.get("menu_estudiante"))

	def sing_up(self):
		"""
		Crear un nuevo usuario
		"""
		nombre = input(Mensajes.mensaje.get("input_name"))
		apellido = input(Mensajes.mensaje.get("input_lastname"))
		correo = input(Mensajes.mensaje.get("input_mail"))
		clave = input(Mensajes.mensaje.get("input_key"))
		fecha_nacimiento = input(Mensajes.mensaje.get("input_birth_date"))
		role = int(input(Mensajes.mensaje.get("input_role")))
		if role == 1:
			usuario = Estudiante(nombre, apellido, correo, clave, fecha_nacimiento)
			Main.lista_estudiante.append(usuario)
			Main.lista_usuarios.append(usuario)
			print(Mensajes.mensaje.get("usuario_created"))
		elif role == 2:
			carrera = input(Mensajes.mensaje.get("input_carer"))
			usuario = Instructor(nombre, apellido, correo, clave, fecha_nacimiento, carrera)
			Main.lista_instructor.append(usuario)
			Main.lista_usuarios.append(usuario)
			print(Mensajes.mensaje.get("usuario_created"))
		else:
			print(Mensajes.mensaje.get("input_error").format(role))
			
	def sing_in(self):
		"""
		Ingresar a la plataforma
		"""
		correo = input(Mensajes.mensaje.get("input_mail"))
		clave = input(Mensajes.mensaje.get("input_key"))
		usuario = Usuario.buscar_por_correo(Main.lista_usuarios, correo)
		role = type (usuario)
		ingresar = usuario.login(clave)
		if (ingresar and isinstance(usuario, Estudiante)):
			Main.display_menu_estudiante()
		elif(ingresar and isinstance(usuario, Instructor)):
			Main.display_menu_instructor()
		else:
			pass


	def read_txt(self):
		pass

	def salir(self):
		sys.exit(0)

	def ingresar_datos_ficticios(self):
		"""Crear Instructor1"""
		instructor1 = Instructor("Juan", "Perez", "Juanpe@instructor.com", "1234", "05-20-1998", "economía")
		Main.lista_instructor.append(instructor1)
		Main.lista_usuarios.append(instructor1)

		"""Crear Estudiante1"""
		estudiante1 = Estudiante("Jorge", "Lopez", "LopezJor@estudiante.com", "2345", "04-07-2005")
		Main.lista_usuarios.append(estudiante1)
		Main.lista_estudiante.append(estudiante1)

		"""Mostrar todos los usuarios registrados (para realizar pruebas)"""
		Main.display_usuarios()

	def run(self):
		while self.break_while:
			Main.display_menu_inicio()
			option = input(Mensajes.mensaje.get("operation"))
			action = self.choices_menu_principal.get(option)
			if action:
				action()
			else:
				print(Mensajes.mensaje.get("input_error").format(option))

if __name__ == "__main__":
	Main().run()
  
"""
		def poblar_txt(self):
		file = open("FicheroInstructor.txt","r")
		for registro in file:
			info = registro.split('@@')
			instruc = Instructor(info[0],info[1],info[2],info[3],info[4],info[5],info[6])
			Instructor.poblar_instructor(instruc, Main.lista_instructor)
		print(Instructor.mostrar_usuarios(Main.lista_instructor))"""

