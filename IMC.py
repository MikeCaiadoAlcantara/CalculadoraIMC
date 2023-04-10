peso = float(input("Digite o seu peso em Kg:"))
alt = float(input("Digite sua altura em metros:"))
imc = peso / alt ** 2

print("Com {:.2f} de altura e {} quilos seu IMC é {:.2f}".format(alt, peso, imc))
if imc <= 18.5:
	print("Cuidado você está a baixo do peso!")
elif imc <= 25:
	print("Parabéns você está no peso ideal!")
elif imc <=	30:
	print("Você está com sobrepeso!")
elif imc <= 34.9:
	print("Cuidado você está com obesidade grau 1!")
elif imc <= 39.9:
	print("Cuidado você está com obesidade grau 2 (SEVERA)!")
else:
	print("Muito cuidado você está com obesidade grau 3 (MÓRBIDA)!")