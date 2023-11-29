import os
#leer archivos
file= open("text.txt",'r')
print(file.read())
file.close()
#editar archivos
file= open("text.txt",'a')
file.write("compeones 2023")
file.close()
#reescribir archivo
file= open("text.txt",'w')
file.write("nuevo 2024")
file.close()
#crear archivo
#file= open("hola.txt",'x')
#file.write("hola mundo")
#file.close()
#elimnar archivo
os.remove('hola.txt')