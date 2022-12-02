# dicionario de ingredientes
# ingredientes[nome] = [unidade, valor]
ingredientes = {}

# dicionario de receita
# receita[nome] = quantidade
receita = {}

# funcao para cadastrar um ingrediente
def cadastrar_ingrediente():
    print("\n>> Cadastrar ingrediente")

    # coleta nome, unidade e valor do ingrediente
    nome, unidade, valor = input("Digite o nome, a unidade e o valor do ingrediente: ").split()
    
    # transforma o valor em float
    valor = float(valor)

    # adiciona ao dicionario de ingredientes o nome como chave e uma lista com unidade e valor como valor
    ingredientes[nome] = [unidade, valor]

# funcao para inserir quantitativo
def inserir_quantitativo():
    print("\n>> Inserir quantitativo")

    # coleta nome e quantidade do ingrediente
    nome, quantidade = input("Digite o nome e a quantidade do ingrediente: ").split()
    
    # transforma a quantidade em float
    quantidade = float(quantidade)

    # adiciona ao dicionario de receita o nome como chave e a quantidade como valor
    receita[nome] = quantidade

# funcao para listar os ingredientes
def listar_ingredientes():
    print("\n>> Listar ingredientes")

    # percorre o dicionario de ingredientes
    for nome in ingredientes:

        # coleta a unidade e o valor do ingrediente
        unidade, valor = ingredientes[nome]

        # imprime o nome, a unidade e o valor do ingrediente
        print(f"{nome} {unidade}: R$ {valor:.2f}")

# funcao para imprimir a receita
def imprimir_receita():
    print("\n>> Imprimir receita")

    # percorre o dicionario de receita
    for nome in receita:

        # coleta a quantidade do ingrediente
        quantidade = receita[nome]

        # verifica se o ingrediente esta cadastrado
        if nome in ingredientes:
            # se sim
            # coleta a unidade e o valor do ingrediente
            unidade, valor = ingredientes[nome]

            # imprime o nome, a quantidade, a unidade e o valor do ingrediente
            print(f"{nome} {quantidade} {unidade}: R$ {quantidade * valor:.2f}")
        else:
            # se nao
            # imprime mensagem de erro
            print(f"{nome} não foi cadastrado")

#  funcao para imprimir o menu
def menu():

    # loop infinito
    while True:

        # imprime o menu
        print("\n>> Sistema de receitas")
        print("1 - Cadastrar ingrediente")
        print("2 - Inserir quantitativo")
        print("3 - Listar ingredientes")
        print("4 - Imprimir receita")
        print("5 - Sair")

        # coleta a opcao do usuario
        opcao = int(input("Digite a opção desejada: "))

        # verifica a opcao
        if opcao == 1:
            cadastrar_ingrediente()
        elif opcao == 2:
            inserir_quantitativo()
        elif opcao == 3:
            listar_ingredientes()
        elif opcao == 4:
            imprimir_receita()
        elif opcao == 5:
            # sai do loop infinito
            break
        else:
            # imprime mensagem de erro
            print("Opção inválida")

# chama a funcao menu
menu()
