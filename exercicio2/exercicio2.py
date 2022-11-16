# Aluno: Raul Fernando Veras Estelita Lafayette
# Matricula: 202203791389

alunos = [[-1 for i in range(4)] for j in range(30)]


def calcular_media(matricula):
    alunos[matricula][3] = (alunos[matricula][0] +
                            alunos[matricula][1] +
                            alunos[matricula][2]) / 3


def lancar_av1():
    matricula, nota = list(map(int, input(
        "Digite a matrícula do aluno e a nota AV1 separados por espaço: "
    ).split()))
    alunos[matricula][0] = nota


def lancar_av2():
    matricula, nota = list(map(int, input(
        "Digite a matrícula do aluno e a nota AV2 separados por espaço: "
    ).split()))
    alunos[matricula][1] = nota


def lancar_av3():
    matricula, nota = list(map(int, input(
        "Digite a matrícula do aluno e a nota AV3 separados por espaço: "
    ).split()))
    alunos[matricula][2] = nota
    calcular_media(matricula)


def listar_aprovados():
    for i in range(len(alunos)):
        if alunos[i][3] >= 7:
            print(f"Matrícula: {i} - Média: {alunos[i][3]}")
    input("Pressione ENTER para continuar...")


def listar_reprovados():
    for i in range(len(alunos)):
        if alunos[i][3] >= 0 and alunos[i][3] < 7:
            print(f"Matrícula: {i} - Média: {alunos[i][3]}")
    input("Pressione ENTER para continuar...")


def menu():
    while True:
        print("MENU")
        print("[1] LANÇAR NOTA AV1")
        print("[2] LANÇAR NOTA AV2")
        print("[3] LANÇAR NOTA AV3")
        print("[4] LISTAR APROVADOS")
        print("[5] LISTAR REPROVADOS")
        print("[0] SAIR")
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
        elif item == "0":
            break
        else:
            print("Opção inválida!")
            input("Pressione ENTER para continuar...")


menu()
