#lanche= ("Hamburguer", "suco", "pizza", "pudim")
#for c in lanche:
    #if c =="suco":
    #    print(f"Eu vou tomar {c} hoje a noite")
    #else:
        #print(f"Eu vou comer {c} hoje a noite")
#for c in range (0,len(lanche)):
    #print (f"Eu vou comer {lanche[c]} na posição {c}")



""" cont = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez")
while True:
    num = int(input("Digite um número entre 0 e 10: "))
    if 0 <= num <= 10:
        break
    print("tente novamente")
print(f"Voce digitou o número {cont[num]}") """




""" times = ("Flamengo" , "Fluminense" , "Cruzeiro" , "Cuiaba" , "Chapecoense", "Atletico-MG", "Atletico", "Atletico-GO")
prim= (times[0:3])
ulti= (times[-3:])
alfa= (sorted(times))
chape= (times.index("Chapecoense"))
print ("-=-=-=-=--=")
print(times)
print ("-=-=-=-=--=")
print(prim)
print ("-=-=-=-=--=")
print(ulti)
print ("-=-=-=-=--=")
print(alfa)
print ("-=-=-=-=--=")
print(f"A Chapecoense está na posição {chape +1}") """


""" from random import randint
sorteio= (randint(0,20), randint(0,20), randint(0,20), randint(0,20), randint(0,20))
menor= min(sorteio)
maior= max(sorteio)
print (f"Sorteei os valores {sorteio}")
print (f"O maior valor foi o número {maior}")
print (f"O menor valor  foi o número {menor}")
"""


""" num=((int(input("Digite um número: "))), (int(input("Digite um número: "))),  (int(input("Digite um número: "))),  (int(input("Digite um número: "))), ) 
cont9=(num.count(9))
print(f'Você digitou os valores {num}')
if 3 in num:
    print(f'O número 3 apareceu primeiro na posição {num.index(3)}')
else:
    print ("Voce não digitou o número 3")
print(f'Você digitou o número 9, {cont9} vezes')
print ("Os valores pares digitados foram ", end='')
for n in num:
    if n%2==0:
        print ( n, end='') """


""" 
lista= ('Pão', 1 
        ,'leite',2.50 , 
        'ovo', 3, 
        'farinha', 100 )

print ("_"*40)
print ("            Lista de Produtos")
print("_"*40)

for itens in range (0 , len(lista)):
    if itens % 2 ==0 :
        print (f"{lista[itens]:.<30}", end='' )
    else:
        print (f"R${lista[itens]:>5}")
print("_"*40) """

""" lista=("aprender",
       'estudar','programar'
       ,'estudante'
       ,'jogo',
       'pipa')
for vogal in lista:
    print (f"\nNa palavra {vogal} temos as vogais ", end='')
    for letra in vogal:
        if letra.lower() in "aeiou":
            print (letra , end=" ") """

