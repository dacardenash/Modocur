#_ guion bajo es para representar que un metodo o varible es privado

from Usuario import Usuario

def poblar_txt():
	file = open("FicheroUsuario.txt","r")
	for registro in file:
		info = registro.split(',')
		usu = Usuario(info[0],info[1],info[2],info[3],info[4],info[5],info[6])
		Usuario.poblar_usuario(usu)
	print(Usuario.mostrar_usuarios())


if __name__ == "__main__":
	poblar_txt()
