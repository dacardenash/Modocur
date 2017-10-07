import sys
from Mensajes import Mensajes
from Instructor import Instructor
from Estudiante import Estudiante

class Main():

	lista_usuarios = []

	def __init__(self):
		self.choices = {
		"1": self.sing_up,
		"2": self.sing_in,
		"3": self.read_txt,
		"4": self.salir
		}
		self.break_while = True

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
		nombre = input(Mensajes.mensaje.get("input_name"))
		apellido = input(Mensajes.mensaje.get("input_lastname"))
		correo = input(Mensajes.mensaje.get("input_mail"))
		clave = input(Mensajes.mensaje.get("input_key"))
		año_de_nacimiento = input(Mensajes.mensaje.get("birth_date"))
		pass

	def sing_in(self):
		pass

	def read_txt(self):
		pass

	def salir(self):
		sys.exit(0)	

	def run(self):
		while self.break_while:
			print(Main.display_menu_inicio())
			option = input(Mensajes.mensaje.get("operation"))
			action = self.choices.get(option)
			if action:
				action()
			else:
				print(Mensajes.mensaje.get("input_error").format(option))

if __name__ == "__main__":
	Main().run()

