#_ guion bajo es para representar que un metodo o varible es privado

import os
from Mensaje import Mensaje
from Instructor import Instructor
from Estudiante import Estudiante
from Usuario import Usuario

class Main():
	lista_instructor = []
	lista_estudiante = []
	lista_comentario = []

	def __init__(self):
		pass

	def poblar_txt(self):
		file = open("FicheroInstructor.txt","r")
		for registro in file:
			info = registro.split('@@')
			instruc = Instructor(info[0],info[1],info[2],info[3],info[4],info[5],info[6])
			Instructor.poblar_instructor(instruc, Main.lista_instructor)
		print(Instructor.mostrar_usuarios(Main.lista_instructor))

	def menu(self):
		print("""
			|---------------------------------------------------------------------------------------|
			|------------------------------ Bienvenido a Modocur :P --------------------------------|
			|---------------------------------------------------------------------------------------|
			""")
		print(Mensaje.menu['opcion1.1'])
		print(Mensaje.menu['opcion1.2'])
		print(Mensaje.menu['opcion1.3'])
		print(Mensaje.menu['opcion1.4'])
		print(Mensaje.menu['opcion1.5'])

		res = 0

		while res != 5:
		
			res = input(Mensaje.label['1'])

			if res == '1':
				#registrar usuario- tipo estudiante
				usuario =  input("Ingrese un nombre: ")
			elif res == '2':
				#login
				mail = input("Ingrese correo electronico: ")
				password = input("Ingrese contraseña: ")
				resul = Usuario.loguear(mail, password, Main.lista_instructor, Main.lista_estudiante)

				if resul == 0:
					print("Su usuario y contraseña son incorrectas")
				elif resul == 1:
					self.menu_instructor()
				elif resul == 2:
					self.menu_estudiante() 	
			elif res == '3':
				#poblar instructores desde txt
				self.poblar_txt()
			elif res == '4':
				#poblar datos
				print("En proceso de desarrollo") 
			elif res == '5':
				os._exit(0)
			else:
				print("Operacion invalida")	


	def menu_instructor(self):
		print("""
			----------------------------------------
			OPERACIONES
			1. Crear curso
			2. Modificar curso
			4. Consultar cursos creados
			3. Comentar
			5. Agregar modulo
			6. Promedio de progreso estudiantes
			7. Cerrar curso   (Cierra el curso y calcula el promedio general de todos los estudiantes)
			8. Mayor promedio de curso
			9. Lista de estudiantes por curso
			----------------------------------------
			""")


	def menu_estudiante(self):
		print("""
			----------------------------------------
			OPERACIONES
			1. Ver curso disponibles
			2. Inscribirse
			3. Ver modulo
			4. Comentar
			5. Ver Progreso cursos realizados
			----------------------------------------
			""")

if __name__ == "__main__":
	#poblar_txt()
	Main().menu()

