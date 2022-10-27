from tkinter import Y


print('Númeors inteiros')
print(1 + 10)
print(11 + 10 + 1000)
print(1.5 + 5 + 0.5)
print(True)
print(False)
print("André Luiz")

#variáveis em Python
#constante: upperCase, espaços: underline
age = 50
name = 'André Luiz'
print('Nome: ', name, '; Idade: ', age)

limite_diario_saque = 1000

BRAZILIAN_STATES = ['São Paulo', 'Sergipe', 'Rio Grande do Sul', 'Goiás', 'Santa Catarina']

print('Saque do dia: ', limite_diario_saque, 'e', 'Estados brasileiros', BRAZILIAN_STATES)

print('Convertendo tipos')

print('Usando int com número decinal 1.9, o resultado é: ', int(1.9))
print(int('9'))
print(float('10.9'))
print('Usando float para imprimir 100 o resultado é: ', float(100))
print('Usando str para converter para string o valor 10.10, o resultado é: ', str(10.10))
print('Exibindo tipo da variável, na conversão do valor 10.10 para string, usando str, o resultado é: ', type(int(10.10)))

valor = 10
valor_str = str(valor)
print('Vendo o tipo da classe: ')
print(type(valor))
print(type(valor_str))

print('Usando a divisão de número inteiro para obter float (valor com casa decimal): ')
print(100/2)
print(100/3)

print('Usando a divisão com de número inteiro, 2 barras //, para obter int (valor sem casa decimal): ')
print(100//2)
print(100//3)

#input | output

nome = input('Digite teu nome: ')
idade = input('Digite a tua idade: ')
print(nome, ',', idade)
print('teste', end=', ')
print(nome, end=', ')
print(idade, end='... \n')
print(nome, idade, sep='#')
print(nome, idade, sep=', ')

#operadores aritméticos
produto_1  = 10
produto_2 = 20
print(produto_1 + produto_2)
print(produto_1 + produto_2 + 3.5)
print(produto_1 - produto_2)
print(produto_1 * produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

#Operadores de comparação

saldo = 200
saque = 200
saque2 = 450

print('Para saldo = 200 e saque = 200')
print('Saldo igual a saque? ', saldo == saque)
print('Saldo diferente de saque? ', saldo != saque)
print('Saldo maior igual a saque? ', saldo >= saque)
print('Saldo menor igual a saque? ', saldo <= saque)
print('Saldo maior que saque? ', saldo > saque)
print('Saldo menor que saque? ', saldo < saque)
print('')
print('Para saldo  = 200 e saque = 450')
print('Saldo igual a saque? ', saldo == saque2)
print('Saldo diferente de saque? ', saldo != saque2)
print('Saldo maior igual a saque? ', saldo >= saque2)
print('Saldo menor igual a saque? ', saldo <= saque2)
print('Saldo maior que saque? ', saldo > saque2)
print('Saldo menor que saque? ', saldo < saque2)

#Operadores de Atribuição simples e complexo

saldo2 = 500
print('O saldo é: ', saldo2)
saldo2 += 500
print('Somando com 500, o saldo será: ', saldo2)
saldo2 -=100
print('Subtraindo 100, o saldo será: ', saldo2)
saldo2 /= 300
print('Dividindo por 300, o saldo será: ', saldo2)
saldo2 *= 2
print('Multiplicando por 2, o saldo será: ', saldo2)
saldo2 //= 3
print('Então, o saldo após a divisão por 3 será: ', saldo2)
saldo2 **= 5
print('Elevando à potência 5, o saldo será: ', saldo2)
saldo2 += 68
print('Somando com 68 o saldo será de: ', saldo2)
saldo2 %= 10
print('10% de 100, o valor será de ', saldo2)

saldo3 = 100
saldo3 %= 10
print('10% do valor de 100 é: ', saldo3)

#Operadores Lógicos
print('Tabelinha dos operadores lógicos')

print('AND: para ser True tudo tem que ser True')
print('True and True = ', True and True)
print('True and False = ', True and False)
print('False and False = ', False and False)

print('OR: para ser True, apenas um tem que ser True')
print('True or True = ', True or True)
print('True or False = ', True or False)
print('False or False = ', False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressão = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print ('A expressão: saldo >= saque and saque <= limite or conta_especial and saldo >= saque será ', expressão)

expressão_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print('A expressão: (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) será ', expressão_2)

conta_simples_com_saldo_suficiente = saldo >= saque and saque <= limite

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

expressão_3 = conta_simples_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print('A comparação da conta simples com a especial tem um valor ', expressão_3)

valor = 10
print(type(valor))

valor2 = '10'
print(type(valor2))

x = '5'
y = '5'
sum = x + y
print(sum, type(sum))

#Operadores de identidade
saldo4 = 1000
limite2 = 500
saldo5 = 500
print('(is) O saldo 1000 e o limite 500 ocupam a mesma região de memória? ', saldo4 is limite2)
print('(is not) O saldo 1000 e o limite 500 ocupam a mesma região de memória? ', saldo4 is not limite2)
print('(is) O saldo 500 e o limite 500 ocupam a mesma região de memória? ', saldo5 is limite2)
print('(is not) O saldo 500 e o limite 500 ocupam a mesma região de memória? ', saldo4 is limite2)

#Operadores de Associação
frutas = ['limao', 'uva', 'laranja']
print('(in) laranja está na lista frutas?', 'laranja' in frutas)
print('(in) Laranja está na lista frutas?', 'Laranja' in frutas)
print('(in) a está na lista frutas?', 'a' in frutas)
print('(in) UVA está na lista frutas?', 'UVA' in frutas)
print('(not in) UVA não está na lista frutas?', 'UVA' not in frutas)
print('(not in) limao não está na lista frutas?', 'limao' not in frutas)
print('(not in) limao não está na lista frutas?', 'limao' not in frutas)

identificacao = 'André Luiz Barbosa'
print('(not in) andré não está na lista frutas?', 'andré' not in frutas)
print('(in) andré está na lista frutas?', 'andré' not in frutas)
print('(not in) Luiz não está na lista frutas?', 'Luiz' not in frutas)
print('(in) Luiz está na lista frutas?', 'Luiz' not in frutas)
print('(not in) Barbosa não está na lista frutas?', 'Barbosa' not in frutas)
print('(in) Barbosa está na lista frutas?', 'Barbosa' not in frutas)

#aspas triplas
Texto = '''Uau... imprime do jeito que eu quero o texto
      muito show      hahahaha      
                     vamos nessa!'''
print(Texto)