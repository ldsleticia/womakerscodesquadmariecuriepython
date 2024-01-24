from functools import reduce

quantidade_de_alunos = 5
quantidade_de_notas_por_aluno = 4
medias_maiores_que_sete = 0
medias = []

for aluno_atual in range(1, quantidade_de_alunos):
    notas_aluno = []
    for nota_atual in range(1, quantidade_de_notas_por_aluno):
        nota_digitada = float(input(f'Digite a nota {nota_atual} do aluno {aluno_atual}: '))
        notas_aluno.append(nota_digitada)
    medias.append(sum(notas_aluno) / len(notas_aluno))

medias_maiores_que_sete = reduce(lambda acc, el: acc + 1 if el >= 7.0 else acc + 0, medias, 0)

print(f'A quantidade de medias maiores que 7 é {medias_maiores_que_sete}')
