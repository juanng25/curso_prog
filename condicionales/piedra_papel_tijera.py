print("Bienvenido a piedra papel tijera")
from random import randint
op = ["piedra","papel","tijera"]#lista de opciones
computer = op[randint(0,2)]#opcion de maquina
player = True #condicion del bucle
while player == True:
	player = input("piedra,papel o tijera?:")#opcion del jugador
	if player == computer:
		print("empate")
	elif player == "piedra":
		if computer == "papel":
			print("Perdistes", computer,">",player)
		else:
			print("Ganastes",player,"<",computer)
	elif player == "papel":
		if computer == "tijera":
			print("Perdistes",computer,"<",player)
		else:
			print("Ganastes",player,">",computer)
	elif player == "tijera":
		if computer == "piedra":
			print("Perdistes",computer,">",player)
		else:
			print("Ganastes",player,"<",computer)
	else:
		print("Error-opcion no valida , intenta escribir las opciones como las vez")
	player = True
	computer = op[randint(0,2)]