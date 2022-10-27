#SAQUE de contas corrente e universitáia
CONTA_NORMAL = False #tipo de liga a conta
CONTA_UNIVERSITARIA = False #tipo de desliga a conta
CONTA_CLASS = True  
SALDO = 2000
SAQUE = 500
CHEQUE_ESPECIAL = 450

if CONTA_NORMAL:
    if SALDO >= SAQUE:
        print('SAQUE realizado com sucesso!')
    elif SAQUE <= (SALDO + CHEQUE_ESPECIAL):
        print('SAQUE realizado com uso de cheque especial')
elif CONTA_UNIVERSITARIA:
    if SALDO >= SAQUE:
        print('SAQUE realizado com sucesso')
    else:
        print('SALDO insuficiente')
elif CONTA_CLASS:
    if SALDO >= SAQUE:
        print('SAQUE realizado da conta class')
    else:
        print('SALDO insuficiente para SAQUE!')
else:
    print('Conta não encontrada, por favor contactar o gerente da conta')
