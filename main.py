from random import randint
a = randint(1, 100)
forse = True
while forse:
	num = int(input("Che numero ho pensato? "))
	if num != a:
		if num > a:
			print("Il numero a cui ho pensato e' piu' piccolo")
		else:
			print("Il numero a cui ho pensa e' piu' grande")
	else:
		print("Bravo!!! Hai infovinato")
		num = False