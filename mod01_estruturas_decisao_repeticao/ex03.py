# Loop infinito para garantir que o usuário forneça uma nota válida
while True:
    # Solicitar ao usuário uma nota entre 0 e 10
    nota = float(input("Digite uma nota entre 0 e 10 (apenas notas redondas, sem vírgula ou ponto): "))
    
    # Verificar se a nota está dentro do intervalo válido
    if 0 <= nota <= 10:
        # Nota válida, sair do loop
        break
    else:
        # Nota inválida, exibir mensagem e continuar no loop
        print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")

# Exibir a nota válida
print(f"Você inseriu a nota: {nota}")
