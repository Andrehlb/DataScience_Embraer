#Identação Blocos

def sacar(valor):
    saldo = 500
    print('Valor de saque 500')
    if saldo >= valor:
        print('Valor liberado!') 
        print('retire teu dinheiro')
    print('Obrigado por ser nosso cliente, tenha um bom dia!')
sacar(100)

#aumentando o valor do saque acima do saldo

def sacar(valor2):
    saldo = 500
    print('Valor de saque 1000')
    if saldo >= valor2:
        print('Valor liberado!')
        print('retire teu dinheiro')
    print('Saldo insuficiente!')
    print('Obrigado por ser nosso cliente, tenha um bom dia!')
sacar(1000)

#estruturas condicionais