
"""
print('-------------------')
print('Um guerreiro Hobbit possuindo \napenas um escudo e armadura\n')
print('foi atingido de raspão da labareda do dragão')
print('-------------------\n')

vida = 10
print(f'sua vida é {vida}')
dano = int(input('Insira qual foi o dano recebido: '))
print(' ')
escudo = 0

if(dano>=vida and escudo == 0):
    print('VOCÊ MORREU! \n')

#dano critico
elif(dano>=5):
    vida = vida - dano
    print('-------------------')
    print('UFA! FOI POR POUCO..  ')
    print(f'VC FICOU COM {vida} de vida.')
    print('-------------------\n')

#dano leve
elif(dano<=5):
    vida = vida - dano
    print('-------------------')
    print('NEM COÇOU  ')
    print(f'VC FICOU COM {vida} de vida.')
    print('-------------------\n')



i=3

while (i<13):
    print(i)
    i += 1


for i in range(3,13):
    print(i)

i=0

while (i<9):
    print(i)
    i+=2

for i in range(0,9,2):
    print(i)



print('----ESCOLHA SEU ITEM -----')
print('(1) COXINHA = R$ 5,00')
print('(2) PASTEL = R$ 7,00')
print('(3) CAFÉ = R$ 4,00')
print('(4) SUCO = R$ 6,00')
print('(5) SAIR ')
print('-------------------------\n')

total = 0

while True:
    item = int(input('Item: '))
    if(item==5):
        break

    quant = int(input('Quantidade: '))
    
    if(item==1):
        total = total + 5 * quant
    elif(item==2):
        total = total + 7 * quant
    elif(item==3):
        total = total + 4 * quant
    elif(item==4):
        total = total + 6 * quant
            
    else:
        print('Digite um valor de Item válido')
    
print(f'Preço total da compra é: {total}')




ticket = 0


while True:
    idade = int(input('Sua idade: '))

    if(idade <= 3):
        print('Ingresso gratuito') 
        break     
    elif(idade>3 and idade<=12):
        ticket=15
        print('Seu Ingresso custa 15,00 reais')
        break
    elif(idade>12):
        ticket=30
        print('Seu Ingresso custa 30,00 reais')
        break
        
"""
#link: https://pt.stackoverflow.com/questions/63097/listar-arquivos-de-um-pasta-em-python
import os

dir = os.listdir('/home/deniken/Python_estudos/')
print(dir)

