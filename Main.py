import sys
from Mensajes import Mensajes
from Instructor import Instructor
from Estudiante import Estudiante
from Usuario import Usuario

class Main():

	lista_instructor = []
	lista_estudiante = []
	lista_comentario = []
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
		self.nombre = input(Mensajes.mensaje.get("input_name"))
		self.apellido = input(Mensajes.mensaje.get("input_lastname"))
		self.correo = input(Mensajes.mensaje.get("input_mail"))
		self.clave = input(Mensajes.mensaje.get("input_key"))
		self.año_nacimiento = input(Mensajes.mensaje.get("birth_date"))
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
  
"""
		def poblar_txt(self):
		file = open("FicheroInstructor.txt","r")
		for registro in file:
			info = registro.split('@@')
			instruc = Instructor(info[0],info[1],info[2],info[3],info[4],info[5],info[6])
			Instructor.poblar_instructor(instruc, Main.lista_instructor)
		print(Instructor.mostrar_usuarios(Main.lista_instructor))"""

