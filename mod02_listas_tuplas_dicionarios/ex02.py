#Exercício 2 Módulo 3
def calcular_medias():
    medias = []  # Lista para armazenar as médias dos alunos
    alunos_com_media_7_ou_mais = 0  # Contador de alunos com média >= 7

    for i in range(5):  # Loop para 5 alunos
        print(f"Aluno {i+1}:")
        total_notas = 0
        for j in range(4):  # Loop para 4 notas
            while True:
                try:
                    nota = float(input(f"Digite a nota {j+1}: "))
                    if 0 <= nota <= 10:  # Verifica se a nota está no intervalo válido
                        break
                    else:
                        print("Por favor, digite uma nota entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")

            total_notas += nota
        media = total_notas / 4
        medias.append(media)  # Adiciona a média na lista

        if media >= 7.0:
            alunos_com_media_7_ou_mais += 1

    print("Médias dos alunos:", medias)
    print(f"Número de alunos com média maior ou igual a 7.0: {alunos_com_media_7_ou_mais}")

calcular_medias()
