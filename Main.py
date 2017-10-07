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
		"0": self.ingresar_datos_ficticios
		}
		self.break_while = True

	def display_usuarios(self):
		for usuario in Main.lista_usuarios:
			print(usuario.to_string())

	def display_instructores(self):
		for instructor in Main.lista_instructor:
			print(instructor.to_string())

	def display_estudiantes(self):
		for estudiante in Main.lista_estudiante:
			print(estudiante.to_string())

	@staticmethod	
	def display_menu_inicio():
		return Mensajes.mensaje.get("menu_inicio")

	@staticmethod
	def display_menu_instructor():
		return Mensajes.mensaje.get("menu_instructor")

	@staticmethod
	def display_menu_estudiante():
		return Mensajes.mensaje.get("menu_estudiante")

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


	def read_txt(self):
		pass

	def salir(self):
		sys.exit(0)	
    
	def run(self):
		while self.break_while:
			print(Main.display_menu_inicio())
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

