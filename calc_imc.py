#código 2 rafgds

print("-------------------Calculadora de IMC-------------------")

nome = (input("Digite o seu nome: "))
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / altura ** 2

print("Olá", nome, ", o seu IMC é de: %.4f" % imc, "isso significa que você está com")

if imc < 16:
    print("magreza grave")
elif imc < 17:
    print("magreza moderada")
elif imc < 18.5:
    print("magreza leve")
elif imc < 25:
    print("saudável")
elif imc < 30:
    print("sobrepeso")
elif imc < 35:
    print("obesidade grau I")
elif imc < 40:
    print("obesidade severa")
else:
    print("obesidade mórbida")
print("-------------FIM------------")
