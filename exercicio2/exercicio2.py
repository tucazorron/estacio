# Aluno: Raul Fernando Veras Estelita Lafayette
# Matricula: 202203791389

# lista de alunos onde cada aluno é uma lista com as notas e a média
alunos = [[-1 for i in range(4)] for j in range(30)]

# calcula a média do aluno e armazena na lista
def calcular_media(matricula):
    # media = (av1 + av2 + av3) / 3
    alunos[matricula][3] = (alunos[matricula][0] + alunos[matricula][1] + alunos[matricula][2]) / 3

# lança a nota da av1
def lancar_av1():
    print("\n>> LANÇAR NOTA AV1")
    # coleta uma lista com dois valores: matricula e nota (ambos string)
    entrada = input("Digite a matrícula do aluno e a nota AV1 separados por espaço: ").split()
    # converte a matricula para inteiro
    matricula = int(entrada[0])
    # converte a nota para float
    nota = float(entrada[1])
    # armazena a nota na lista de alunos na primeira posição
    alunos[matricula - 1][0] = nota

# lança a nota da av2 
def lancar_av2():
    print("\n>> LANÇAR NOTA AV2")
    # coleta uma lista com dois valores: matricula e nota (ambos string)
    entrada = input("Digite a matrícula do aluno e a nota AV2 separados por espaço: ").split()
    # converte a matricula para inteiro
    matricula = int(entrada[0])
    # converte a nota para float
    nota = float(entrada[1])
    # armazena a nota na lista de alunos na segunda posição
    alunos[matricula - 1][1] = nota

# lança a nota da av3
def lancar_av3():
    print("\n>> LANÇAR NOTA AV3")
    # coleta uma lista com dois valores: matricula e nota (ambos string)
    entrada = input("Digite a matrícula do aluno e a nota AV3 separados por espaço: ").split()
    # converte a matricula para inteiro
    matricula = int(entrada[0])
    # converte a nota para float
    nota = float(entrada[1])
    # armazena a nota na lista de alunos na terceira posição
    alunos[matricula - 1][2] = nota
    # calcula a média do aluno
    calcular_media(matricula - 1)

# lista os alunos aprovados
def listar_aprovados():
    print("\n>> LISTAR APROVADOS")
    # percorre a lista de alunos
    for i in range(len(alunos)):
        # se a média for maior ou igual a 7
        if alunos[i][3] >= 7:
            # imprime a matricula e a média
            print(f"Matrícula: {i + 1} - Média: {alunos[i][3]}")
    input("Pressione ENTER para continuar...")

# lista os alunos reprovados
def listar_reprovados():
    print("\n>> LISTAR REPROVADOS")
    # percorre a lista de alunos
    for i in range(len(alunos)):
        # se a média for menor que 7 e maior ou igual a 0
        if alunos[i][3] >= 0 and alunos[i][3] < 7:
            # imprime a matricula e a média
            print(f"Matrícula: {i + 1} - Média: {alunos[i][3]}")
    input("Pressione ENTER para continuar...")

# menu principal
def menu():
    # loop infinito
    while True:
        print("\nMENU")
        print("[1] LANÇAR NOTA AV1")
        print("[2] LANÇAR NOTA AV2")
        print("[3] LANÇAR NOTA AV3")
        print("[4] LISTAR APROVADOS")
        print("[5] LISTAR REPROVADOS")
        print("[0] SAIR")
        # coleta a opção do usuário
        item = input("Digite a opção desejada: ")
        if item == "1":
            lancar_av1()
        elif item == "2":
            lancar_av2()
        elif item == "3":
            lancar_av3()
        elif item == "4":
            listar_aprovados()
        elif item == "5":
            listar_reprovados()
        # se a opção for 0, sai do loop
        elif item == "0":
            break
        # se a opção for inválida, imprime uma mensagem de erro
        else:
            print("Opção inválida!")
            input("Pressione ENTER para continuar...")

menu()
