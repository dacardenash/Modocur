import sys
from Mensajes import Mensajes
from Instructor import Instructor
from Estudiante import Estudiante

class Main():

	def __init__(self):
		"1": self.sing_up,
       	"2": self.sing_in,
       	"3": self.read_txt,
       	"4": self.salir,


	def poblar_txt(self):
		file = open("FicheroInstructor.txt","r")
		for registro in file:
			info = registro.split('@@')
			instruc = Instructor(info[0],info[1],info[2],info[3],info[4],info[5],info[6])
			Instructor.poblar_usuario(instruc)
		print(Instructor.mostrar_usuarios())

	""" def run(self):
		print(Mensajes.mensaje.get("menu"))

		res = input(Mensajes.mensaje.get("operation"))

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
	""" 

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
	Main().run()

