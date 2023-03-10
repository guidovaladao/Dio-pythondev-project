# criar um sistema bancário simples.
# depósito, saque e extrato.

# 1 = depósito
# 2 = saque
# 3 = extrato
# 4 = sair

print('d = Fazer depósito.\ns = Saque.\ne = Ver extrato.\nq = Sair.')

extrato = ''
saldo = 100
ls = 0
limite_saque = 3
valor_limite_saque = 500

while (True):

    opcao = (input('\nDigite a função desejada: '))

    if (opcao == 'd'):
        valor_deposito = float(input('Informe o valor do depósito: '))
        if (valor_deposito > 0):
            saldo = saldo + valor_deposito
            extrato += (f'Depósito: R$ {valor_deposito:.2f}\n')
            print('Depósito realizado com sucesso!')
        else:
            print('Operação falhou! O valor informado é inválido!')

    elif (opcao == 's'):
        valor_saque = float(input('Informe o valor do saque: '))

        excedeu_limite_saque = valor_saque > valor_limite_saque
        excedeu_saldo = valor_saque > saldo
        excedeu_tentativas = ls >= limite_saque

        if (excedeu_saldo):
            print('Saldo insuficiente!')
        elif (excedeu_tentativas):
            print('Número de saques diários atingido!')
        elif (excedeu_limite_saque):
            print('O valor máximo de cada saque é de R$ 500,00!')
        elif (valor_saque > 0):
            saldo -= valor_saque
            extrato += (f'Saque: R$ {valor_saque:.2f}\n')
            print('Saque realizado com sucesso!')
            ls += 1
        else:
            print('Informe um valor válido!')
    elif (opcao == 'e'):
        print('-----------------------------------')
        print('Imprimindo extrato...')
        print('\n########################## Extrato ##########################')
        if (len(extrato) == 0):
            print('Não foram realizadas movimentações em sua conta.')
            print(f'\nSaldo: R$ {saldo:.2f}')
            print('#############################################################')
        else:
            print(f'\nSaldo: R$ {saldo:.2f}')
            print('#############################################################')
    elif (opcao == 'q'):
        print('Obrigado por utilizar nossos sistemas! Até logo!')
        break
    else:
        print('Informe uma opção válida!')










