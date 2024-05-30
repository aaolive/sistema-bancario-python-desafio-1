# funcoes basicas de banco

saldo = 1000.0
valor = 0.0

historico_movimentos = {}

def depositar(valor=0.0):
    global saldo # se refere a variavel global externa
    saldo += valor
    print("Deposito concluido. Saldo atual: " + str(saldo))


def sacar(valor=0.0):
    global saldo
    if valor > 0 and valor <= saldo:
        saldo -= valor
        print('Seu saldo atual: ' + str(saldo))

def ver_extrato():
    pass

# metodo para operar o app
def excutar_app():
    resposta = 's'
    while resposta == 's':
        print("Acessando o sistema do banco...\n")
        operar_conta()
        print('Deseja continuar acessando o banco? (s/n).')
        resposta = input()
    
# metodo para usar o banco
def operar_conta():
    print(f'Saldo atual da conta: {saldo}')
    print('''Escolha uma operacao de conta:
          1 - sacar
          2 - depositar
          3 - extrato ''')
    
operar_conta()

# Faz o processamento da opcao escolhida
opcao = input()

if opcao == '1':
    print('## Operacao de saque ##')
    valor_do_saque = float(input('Informe o valor do saque: '))
    sacar(valor_do_saque)

elif opcao == '2':
    print('## Operacao de deposito ##')
    valor_do_deposito = float(input('Informe o valor do deposito: '))
    depositar(valor_do_deposito)
    pass
elif opcao == '3':
    pass

# executa o banco
#excutar_app()