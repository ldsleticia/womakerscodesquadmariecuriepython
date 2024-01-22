idade = int(input("Digite a idade: "))

if idade <= 11:
    print("Criança")
elif 12 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else:
    print("Idoso")
