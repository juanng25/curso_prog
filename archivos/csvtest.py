import csv
with open('animes.csv') as file:
	reader= csv.DictReader(file)
	for row in reader:
		print(row['nombre'])

with open('animes.csv','w') as file:
	writer= csv.writer(file)
	writer.writerow([4,"naruto","naruto"])
	