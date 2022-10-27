from xml.sax.xmlreader import InputSource

print('Licença para obter CNH')
MAIOR_DE_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input('Digite a tua idade: '))

if idade >= MAIOR_DE_IDADE:
    print('Você já é maior de idade, já pode tirar tua CNH.')

if idade < MAIOR_DE_IDADE:
    print('Você ainda não tem a idade mínima exigida para tirar tua CNH.')

    #uso do elif
    #será adicionada a regra idade especial

if idade >= MAIOR_DE_IDADE:
    print('Você já é maior de idade, já pode tirar tua CNH.')

elif IDADE_ESPECIAL >= 12:
    print('Permissão para fazer, apenas, aulas teóricas')

if idade < MAIOR_DE_IDADE:
    print('Você ainda não tem a idade mínima exigida para tirar tua CNH.')


#outra forma, mais enxuta, licença para helicóptero
#de acordo com os actuais regulamentos 
#da Agência Federal da aviação, 
# deve: Ter 17 anos ou mais

print('Licença para pilotar helicóptero')
MAIOR_DE_IDADE_Helicoptero = 17

idade_helicoptero = int(input('Digite a tua idade: '))

if idade_helicoptero >= MAIOR_DE_IDADE_Helicoptero:
    print('Você tem mais de 17 anos, então já pode tirar tua licença.')

else:
    print('Você ainda não tem a idade mínima exigida para tirar tua licença.')

