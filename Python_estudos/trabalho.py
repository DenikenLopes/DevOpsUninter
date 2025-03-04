"""
#QUESTÃO 1 de 4

desconto = 0
print('\n')
print('-'*25)
print('Bem vindo a Loja do Deniken \n')
valor= float(input('Entre com o valor do produto: '))
quant= int(input('Entre com a quantidade do Produto: '))
print('-'*25)


if(valor>0):

    valor = valor * quant
    
    if (valor<2500): #sem desconto 
        
        print('Você não recebeu desconto')
        
    elif (valor>=2500 and valor<6000): #desconto de 4%
    
        desconto = valor - valor * 0.04 
        
    elif (valor>=6000 and valor<10000): #desconto de 7%
    
        desconto = valor - valor * 0.07

    elif (valor>=10000): #desconto de 11%
    
        desconto = valor - valor * 0.11
    
else:
    print('Você não Digitou um valor válido')


print(f'O valor SEM desconto: {valor}')
print(f'O valor COM desconto é de: {desconto}')



#QUESTÃO 2 de 4


print('\nBem vindo a Loja de Gelados do Deniken \n')
print('-'*20+'CARDÁPIO'+'-'*20)
print('-'*48)
print('---| tamanho |   cupuaçu (CP)  |  Açaí (AC) |---')
print('-'*48)
print('---|    P    |    R$  9,00     |  R$ 11,00  |---')
print('---|    M    |    R$ 14,00     |  R$ 16,00  |---')
print('---|    G    |    R$ 18,00     |  R$ 20,00  |---')
print('-'*48)

#variáveis de preço do cupuaçú
c_p = 9.0
c_m = 14.0
c_g = 18.0

#variáveis de preço do Açaí
a_p = 11.0
a_m = 16.0
a_g = 20.0

total = 0

while True:
    
        sabor=input('Escolha um sabor(cp/ac): ')

        if(sabor != 'ac' and sabor != 'cp'):  #validando sabor
            print('Sabor inválido')
            continue
            
        elif(sabor=='ac'):
                        
            tam=input('Qual o tamanho?: ')
            
            #Condição/acumulador de preço
            if(tam=='p'):
                 total += a_p
            elif(tam=='m'):
                 total += a_m
            elif(tam=='g'):
                total += a_g

            while(tam!='p' and tam!='m' and tam!='g'): #validando tamanho
                print('Tamanho inválido!')
                tam=input('Qual o tamanho?: (P/M/G)')
                continue
            else:
                print(f'Você escolheu o tamanho:{tam}')
                a=input('Deseja fazer outro pedido? (S/N): ')
                if(a=='s'):
                    continue
                else:
                     break
                
        elif(sabor=='cp'):
                        
            tam=input('Qual o tamanho? (P/M/G): ')

            #Condição/acumulador de preço
            if(tam=='p'):
                total += c_p
            elif(tam=='m'):
                total += c_m
            elif(tam=='g'):
                total += c_g


            while(tam!='p' and tam!='m' and tam!='g'): #validando tamanho
                print('Tamanho inválido!')
                tam=input('Qual o tamanho?: ')
                continue
            else:
                print(f'Você escolheu o tamanho:{tam}')
                a=input('Deseja fazer outro pedido? (S/N): ')
                if(a=='s'):
                    continue
                else:
                     break
                


print(f'total a pagar é: R$ {total} Reais')



#QUESTÃO 3 de 4

v_dig=1.10
v_ico=1.0
v_ipb=0.40
v_fot=0.20
v_pag=0

#função escolher serviço
def escolha_servico():
    while True:

        serv=input('Escolha um serviço: ')
        if(serv=='dig'):
            preco = v_dig
            break            
        elif(serv=='ico'):
            preco = v_ico
            break
        elif(serv=='ipb'):
            preco = v_ipb
            break
        elif(serv=='fot'):
            preco = v_fot
            break 
        elif(serv=='pag'):
            preco = v_pag
            break
        else:
            print('Digite um serviço válido')
            continue
    return preco

#função escolher numero de página
def num_pagina():
    while True:
        try:
            quant=int(input('Quantas páginas?: '))

            if(quant>=20000):
                print('Não é aceito essa quantidade de página!')
                continue
            elif(quant>=2000 and quant<20000):
                desconto=0.25
                break
            elif(quant>=200 and quant<2000):
                desconto=0.20
                break
            elif(quant>=20 and quant<200):
                desconto=0.15
                break
            elif(quant<20 and quant>0):
                desconto=0
                break
        except ValueError:
            print('Entre com uma opção válida!')
            continue
    return desconto

#função serviço extra
def servico_extra():
    
    while True:
        try:
            serv=int(input('Escolha um serviço adicional de: '))
            if(serv>=0 and serv<3):
                if(serv==1): #encadernação simples
                    add=15.0
                    break
                elif(serv==2):#encadernação capa dura
                    add=40.0
                    break
                elif(serv==0):#nenhuma encadernação
                    add=0
                    break
                
        except ValueError:
            print('Entre com uma opção válida!')
            continue
    
    return add


print('-'*51)
print('---Bem vindo a copiadora do Deniken---')
print('-'*51)
print('-----------Escolha o Serviço----------')
print('-'*51)
print('---------> (dig) digitalização  R$ 1,10') 
print('---------> (ico) Impressão colorida  R$ 1,00 ')
print('---------> (ipb) Impressão Preto e Branco  R$ 0,40')
print('---------> (fot) Fotocópia  R$ 0,20 ')
print('-'*51)
print('ENCADERNAÇÃO: SIMPLES(1) - CAPADURA(2) - NENHUMA(0)')
print('-'*51)

serv=escolha_servico()
pagina=num_pagina()
extra=servico_extra()
print(f'serviço é de: R$ {serv},\nO valor por página: R$ {pagina},\nO serviço extra é de: R$ {extra} ')

total=(serv*pagina) + extra

print('-'*51)
print(f'O valor total do serviço é de: {total}')
print('-'*51)


lista_livro=[]
global id = 0


print('Seja bem vindo a livraria do Deniken')
print('MENU PRINCIPAL')
print('Escolha a opção desejada')
print('(1) Cadastrar livro')
print('(2) Consultar livro')
print('(3) Remover livro')
print('(4) Encerrar Programa')


print('MENU CADASTRAR LIVRO')
print('(1) Consultar todos')
print('(2) Consultar por ID')
print('(3) Remover por Autor')
print('(4) Retornar')





person = ('Mario','Luigi','Yoshi','Bowser') #<---tuplas

for palavra in person:
    print(f'\n{palavra.lower()}')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
        


import random

def valida_int(pergunta, min, max):
    x=int(input(pergunta))
    while(x<min or x>max):
        x=int(input(pergunta))
    return x


def vencedor(jogador1,jogador2):

    global v1, v2, empate

    if jogador1 == 1: #pedra 
        if jogador2 == 1: #Pedra
            empate += 1
        elif jogador2 == 2: #Papel
            v2 += 1
        elif jogador2 == 3: #Tesoura
            v1 += 1
               
    elif jogador1 == 2: #papel
        if jogador2 == 1: #Pedra
            v1 += 1
        elif jogador2 == 2: #Papel
            empate += 1
        elif jogador2 == 3: #Tesoura
            v2 += 1        

    elif jogador1 == 3 : #tesoura
        if jogador2 == 1: #Pedra
            v2 += 1
        elif jogador2 == 2: #Papel
            v1 += 1
        elif jogador2 == 3: #Tesoura
            empate += 1        

    resultado = [v1,v2,empate]  
    return resultado  
    


print('(1) PEDRA')
print('(2) PAPEL')
print('(3) TESOURA')
print('(0) SAIR')

jogadas = []
resultado = []

#variáveis globais
v1 = 0
v2 = 0
empate = 0


while True:
    j1 = valida_int('Escolha sua jogada', 0,3)
    if not j1: #se digitar 0 sai
        break
    j2 = random.randint(1,3) #randomiza os numeros contidos
    jogadas.append([j1,j2]) #adiciona em uma lista conteúdo das jogadas dos jogadores

    resultado = vencedor(j1,j2) #função vencedor


#entrada de dados
j1 = valida_int('Escolha sua jogada: ', 0,3) #entrada e validação
j2 = random.randint(1,3) #randomiza escolha jogador2/computador

jogadas.extend([j1,j2]) #adiciona em uma lista
print(f'jogadas: {jogadas[0]}')
print(f'jogadas: {jogadas[1]}')

resultado = vencedor(j1,j2) #função vencedor

print(f'Se 1, jogador1 ganhou: {resultado[0]}')
print(f'Se 1, Computador ganhou: {resultado[1]}')
print(f'Se 1, deu empate : {resultado[2]}')



# dicionário = {'nome':[], 'endereco':[]}
# lista = [nome1, nome2, 1, 2, 3]
# tuplas = (nome, endereco) #dados fixos



cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    validar = input('Deseja cadastra uma pessoa? : ')
    if validar.upper() in 'N':
        break
    if validar.upper() not in 'S':
        continue
    

    nome = input('Qual o nome: ')
    sexo = input('Qual o sexo: ')
    ano = input('Qual o ano: ')

    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)

nome = (a,1,3)


mochila = {'a':['Bota',20], 'b':['Machado', 2], 'c':['antidoto', 3]}

#mochila[input('Escolha o bolso da mochila [a/b/c]: ')].append(input('entre com o item: '))


print(mochila)

#print(mochila[1][0])

"""
#mochila = {'a':['Bota',20], 'b':['Machado', 2], 'c':['antidoto', 3]}
#link: http://devfuria.com.br/python/manipulando-arquivos-de-texto/ 

arq='arquivo.txt'
a=open(arq , 'r')
conteudo = a.readlines()
conteudo.append('entrando com uma nova linha')

a=open(arq , 'w')
a.writelines(conteudo)
a.close()

#a.write(f'{mochila}\n')
#guardar = a.read()
#print(f'este é o conteudo do arquivo: {guardar}')
a.close()
