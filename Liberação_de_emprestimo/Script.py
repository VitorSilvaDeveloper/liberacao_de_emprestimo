salario = int(input('Digite o valor do salario(sem pontos): R$'))
quantidade = int(input('Quanto deseja pegar(sem pontos): R$'))
parcelas = int(input('Em quantas parcelas deseja pagar? '))

#Banco não pode descontar mais de 30% do salário de cliente para cobrir débito. 
#Pegando 30% do salario para verificação.
def porcentagem():
    porcentagem = salario*0.30
    return porcentagem
porcentagem_final = porcentagem()

#Calculando a mensalidade já com juros.
def conta():
    mensalidade = quantidade/parcelas
    taxa_juros = quantidade*0.03
    novo_valor = mensalidade + taxa_juros
    return novo_valor
mensalidade_verificada = conta()


valor_final = parcelas*mensalidade_verificada

#Verificando se a mensalidade é menor que 30% do sálario para liberação.
def liberacao_reprovado():
    if mensalidade_verificada <= porcentagem_final:
        print('Aprovado')
        print(f'O valor finaciado foi de R${valor_final} da sua parcela ficou de R${mensalidade_verificada:.2f}')
    else:
        print('Valor reprovado tente um pedido mais baixo.')


print('Caso o valor aprovado. será adicionado 3% de juros por mês.')
continuacao = str(input('todos de acordo? aperte qualquer tecla para continuar..'))

liberacao_reprovado()