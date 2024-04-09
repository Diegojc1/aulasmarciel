sexo = input("Informe o seu sexo (M para masculino, F para feminino): ").strip().upper()
altura = float(input("Informe a sua altura em metros (ex: 1.75): "))

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo informado é inválido.")
    exit()

print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
