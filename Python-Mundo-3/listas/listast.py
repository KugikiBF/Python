""" valores= []
for c in range(0,5):
    valores.append(int(input("Digite um valor: ")))
    maior= max(valores)
    menor= min(valores)
print(f"O maior valor foi {maior} na posição ", end='')
for i,v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f"O menor valor foi {menor} na posição ", end='') 
for i,v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='') """


""" listanum=[]
while "True":
    adicionar=(int(input("Digite um valor: ")))
    continuar= str(input("Você quer continuar? [S/N] ")).capitalize()
    if adicionar not in listanum:
        listanum.append(adicionar)
    else:
        print("Esse dado já está inserido, não vou reproduzi-lo.")
    if continuar == "N":
        break
    while continuar not in "S":
        continuar= str(input("Você quer continuar? [S/N] ")).capitalize()
        if continuar == "N":
            break
listanum.sort()
print(listanum)
         """

""" valores= list()
for c in range(0,5):
    num= int(input("Digite um valor: "))
    if c == 0 or num> valores[-1]:
        valores.append(num)
    else:
        pos=0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos+=1
print(valores) """


""" valores=list()
while True:
    while True:
        try:
            num= int(input("Digite um número: "))
            break
        except ValueError:
            print("Voce digitou um número inválido.")
    valores.append(num)
    prosseguir= str(input("Quer continuar [S/N] ")).upper() .strip()
    while prosseguir not in ('N','S'):
        prosseguir = input("Dados inválidos! Digite apenas [S/N]").upper()
    if prosseguir =="N":
        break
valores.sort(reverse=True)
print(f'Voce digitou {len(valores)} elementos.')
print(f'Os valores digitados em ordem decrescente foram {valores}')
if 5 in valores:
    print("O valor 5 faz parte da lista")
else:
    print('O valor 5 não faz parte de lista') """


        
""" valores=list()
pares=[]
impares=[]
while True:
    while True:
        try:
            num=int(input("Digite um valor: "))
            break
        except ValueError:
            print("Erro! Dado inválido")
    valores.append(num)
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)
    continuar= input("Quer continuar? [S/N] ").upper() .strip()
    while continuar not in ("S","N"):
        continuar= input("Dados inválidos! Quer continuar? [S/N] ").upper() .strip()
    if continuar == "N":
        break
print(f'A lista completa é {valores}')
print(f'Os pares são {pares}')
print(f'Os impares são {impares}') """




""" exp=()
exp=(input("Digite a expressão: "))
print(f"{exp.count("(")}") """


""" expr= (input("Digite a expressão: "))
pilha=[]
for simbolo in expr:
    if simbolo =="(":
        pilha.append("(")
    elif simbolo ==")":
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) ==0:
    print("Sua expressão está válida")
else:
    print("Expressão inválida") """



