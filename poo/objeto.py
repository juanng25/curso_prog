class Carro:
	motor="v8"
	encendido=False
	def __init__(self,marca,modelo,color):
		self.marca=marca
		self.modelo=modelo
		self.color=color

	def arranque(self):
		self.encendido=True
		print("runrunrun")

juan=Carro("toyota","prado","gris")
juan.arranque()
eric=Carro("lexuus","ux","negro")
david=Carro("honda","hrv","blanco")
david.color="negro"
carros=[juan,eric,david]

for carro in carros:
	print(carro.modelo)
	print(carro.encendido)
	print(carro.color)