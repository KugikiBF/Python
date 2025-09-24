""" galera= list()
dados=list()
maior=menor=0
while True:
    dados.append(input("Nome: ").capitalize())
    while True:
        try:
            dados.append(float(input("Peso: ")))
            break
        except ValueError:  print("Dado inválido!")
    if len(galera) == 0:
        maior=menor = dados[1]
    else:
        if maior< dados[1]:
            maior=dados[1]
        if dados[1]< menor:
            menor= dados[1]
    galera.append(dados[:])
    dados.clear()
    continuar=input("Voce quer continuar? [S/N] ").upper().strip()
    while continuar not in ("S","N"):
        continuar=input("Dado inválido! Digite apenas:[S/N] ").upper().strip()
    if continuar == "N": break

print(f'Voce cadastrou {len(galera)} pessoas.')
print(f'O maior peso registrado foi {maior}KG das pessoas ', end='')
for p in galera:
    if p[1] ==maior:
        print(f'[{p[0]}]', end=' ')
print("")
print(f'O menor peso registrado foi {menor}KG das pessoas ', end='')
for p in galera:
    if p[1]==menor:
        print(f'[{p[0]}]',end=' ')      
         """



""" impar=list()
par=[]
for c in range(1,8):
    impar.append(int(input(f"Digite o {c}° valor: ")))
    if impar[-1]%2==0:
        par.append(impar[-1])
        impar.pop()
print(par)
print(impar) """


""" num=[[], []]
valor=0
for c in range(1,8):
    valor=int(input(f"Digite o {c}° valor: "))
    if valor%2==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(num) """



""" matriz=[[ 0, 0, 0 ],
        [ 0, 0, 0 ],
        [ 0, 0, 0 ]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um Valor para a posição [{l}:{c}]: "))
print(matriz[0])
print(matriz[1])
print(matriz[2]) """

