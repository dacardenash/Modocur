#_ guion bajo es para representar que un metodo o varible es privado

import sys
from Mensaje import Mensaje
from Instructor import Instructor
from Estudiante import Estudiante

class Main():

	def __init__(self):


	def poblar_txt(self):
		file = open("FicheroInstructor.txt","r")
		for registro in file:
			info = registro.split('@@')
			instruc = Instructor(info[0],info[1],info[2],info[3],info[4],info[5],info[6])
			Instructor.poblar_usuario(instruc)
		print(Instructor.mostrar_usuarios())

	def menu(self):
		print("""
			|---------------------------------------------------------------------------------------|
			|------------------------------ Bienvenido a SIA 2.0 :P --------------------------------|
			|---------------------------------------------------------------------------------------|
			""")
		print(Mensaje.menu['opcion1.1'])
		print(Mensaje.menu['opcion1.2'])
		print(Mensaje.menu['opcion1.3'])
		print(Mensaje.menu['opcion1.4'])
		print(Mensaje.menu['opcion1.5'])

		res = input(Mensaje.label['1'])

		if res == '1':
			#registrar usuario- tipo estudiante
			usuario =  input("Ingrese un nombre: ")
		elif res == '2':
			#login
			mail = input("Ingrese correo electronico: ")
			password = input("Ingrese contraseña: ")
		elif res == '3':
			#poblar instructores desde txt
			self.poblar_txt()
		elif res == '4':
			#poblar datos
			print("En proceso de desarrollo") 
		elif res == '5':
			#salir aplicacion
			sys.exit()
		else:
			print("Operacion invalida")	

	def menu_instructor(self):
		print("""
			OPERACIONES
			1. Crear curso
			2. Modificar curso
			3. 
			""")


	def menu_estudiante(self):
		print("""
			OPERACIONES
			""")

if __name__ == "__main__":
	#poblar_txt()
	Main().menu()

