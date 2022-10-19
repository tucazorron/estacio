# Aluno: Raul Fernando Veras Estelita Lafayette
# Matricula: 202203791389

# importa a biblioteca math para usar a funcao math.ceil()
import math

# constante afirmada na descricao do exercicio
produtividade = 7

# coleta do usuario a quantidade de armacoes
quantidade_armacoes = int(input("(Inteiro) Digite a quantidade de armações: "))

# coleta do usuario a quantidade de armadores
quantidade_armadores = int(input("(Inteiro) Digite a quantidade de armadores: "))

# coleta do usuario a jornada diaria de trabalho
jornada_diaria = int(input("(Inteiro) Digite a jornada diária: "))

# calcula qual sera a duracao do servico
duracao_servico = quantidade_armacoes / (produtividade * quantidade_armadores * jornada_diaria)

# arredonda a duracao do servico para um valor inteiro que seja maior ou igual ao valor original
duracao_servico_ceil = math.ceil(duracao_servico)

# imprime o numero aproximado de dias que o servico durara
print(f"A duração do serviço será de aproximadamente {duracao_servico_ceil} dias.")

# imprime o numero exato de dias que o servico durara
print(f"Pra ser exato, o serviço durará {duracao_servico} dias.")

# caso o servico dure mais que 10 dias
if duracao_servico > 10:
    # imprime a mensagem de contratacoes
    print("Obs: É preciso contratar mais armadores.")
