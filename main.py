from random import randint
a = randint(1, 100)
forse = True
<<<<<<< HEAD
while forse:
	num = int(input("Che numero ho pensato? "))
	if num != a:
=======
count = 0
while forse:
	num = int(input("Che numero ho pensato? "))
	if num != a:
		count += 1
>>>>>>> feature
		if num > a:
			print("Il numero a cui ho pensato e' piu' piccolo")
		else:
			print("Il numero a cui ho pensa e' piu' grande")
	else:
<<<<<<< HEAD
		print("Bravo!!! Hai infovinato")
=======
		print("Bravo!!! Hai infovinato in {} tentativi".format(count))
>>>>>>> feature
		num = False