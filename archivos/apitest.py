import requests
respuesta= requests.get('https://swapi.dev/api/people/')
data= respuesta.json()
for planeta in data['results']:
	print(planeta['name'])