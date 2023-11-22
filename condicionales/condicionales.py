#if else
edad= input("Cuantos anos tienes..")
edad=int(edad)
if edad<3:
	print("eres un bebe")
elif edad<17:
	print("aun te falta")
elif edad>80:
	print("ya muerete")
else:
	print("eres un adulto")
#while
a = 1
while a<11:
	print(a)
	a += 1
#for
a= ["uno","dos","tres"]
x= 0
for num in a:
	x=x+1
	print(x)	