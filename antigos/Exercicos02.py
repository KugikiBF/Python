# cont=soma=0
# while True:
#     n=int(input("Digite um valor: "))
#     if n == 999:
#         break
#     soma+=n
#     cont+=1
# print(f"A soma dos {cont} valores foi de {soma}!") 









# while True:
    # n= int(input("Quer ver a tabuada de que valor? "))
    # if n<0:
    #     break
    # for c in range(1,11):
    #     print(F"{n} x {c} = {n*c}")












# from random import randint
# cont=0
# print("=-"*20)
# print("vamos jogar par ou impar".upper())
# print("=-"*20)
# while True:
#     n=int(input("Digite um valor: "))
#     j= " "
#     while j not in "pPiI":
#         j=(input("Escolha par ou ímpar[P/I] ".upper()).upper()).upper()[0]
#     print("-"*40)
#     comp=randint(0,10)
#     soma=n+comp
#     if soma%2==0 and j=="P":
#         cont+=1
#         print(F"Voce jogou {n} e o computador {comp}. Total de {soma} deu par")
#         print("-"*40)
#         print("voce ganhou".upper())
#         print("Vamos jogar novamente...")
#         print("=-"*20)
#     if soma%2!=0 and j=="I":
#         cont+=1
#         print(F"Voce jogou {n} e o computador {comp}. Total de {soma} deu impar")
#         print("-"*40)
#         print("voce ganhou".upper())
#         print("Vamos jogar novamente...")
#         print("=-"*20)
#     if soma%2==0 and j=="I":
#         print(f"GAME OVER! Voce venceu {cont} vezes.")
#         break
#     if soma%2!=0 and j=="P":
#         print(f"GAME OVER! Voce venceu {cont} vezes.")
#         break







# cont=contHomem=contmulher=0
# print("__"*15)
# print("     cadastre uma pessoa".upper())
# print("__"*15)
# while True:
#     id=int(input("Digite sua idade: "))
#     sexo=c= " "
#     while sexo not in "MF":
#         sexo=(input("Digite seu sexo[M/F]: ")).strip().upper()[0]
#     if id>=18: 
#         cont+=1
#     if sexo in "mM":
#         contHomem+=1
#     if sexo=="F" and id<=20:
#         contmulher+=1
#     while c not in "SN":
#         c=(input("Voce quer continuar[S/N]? ")).strip().upper()[0]
#     if c in "N":
#         break
#     print("__"*15)
#     print("    cadastre outra pessoa".upper())
#     print("__"*15)
# print(f"Tem {cont} pessoas com mais de 18 anos")
# print(F"Tem {contHomem} homens cadastrados")
# print(F"Tem {contmulher} mulheres com menos de 20 anos")







# mais=soma=barato=cont=0
# bara=" "
# print('--'*15)
# print("         LOJA BARATA")
# print('--'*15)
# while True:
#     pros= " "
#     produto=str(input("Digite um produto: ").capitalize())
#     preço=float(input("Digite seu valor: R$").replace(",","."))
#     while pros not in "NS":
#         pros=str(input("Deseja continuar[S/N]? ").capitalize().strip())[0]
#     print('__'*15)
#     soma+=preço
#     cont+=1
#     if cont==1 or preço<barato:
#         barato=preço
#         bara=produto
#     if preço>=1000:
#         mais+=1
#     if pros in "nN":
#         break
# print(f"\033[34mo total foi de {soma}")
# print(f'{mais} produtos custam mais de R$1000 ')
# print(f"o nome do produto mais barato é {bara}\033[m")





from time import sleep
print("="*30)
print("Banco top".center(30).upper())
print("="*30)
sac=int(input("Qual valor deseja sacar? R$"))
total=sac
cedula=200
cont=0
print("processando...".upper())
sleep(0.8)
while True:
    if total>=cedula:
        total-=cedula
        cont+=1
    else:
        if cont!=0:
            print(f"Total de {cont} de R${cedula}")
        if cedula==200:
            cedula=100
        elif cedula==100:
            cedula=50
        elif cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=5
        elif cedula==5:
            cedula=1
        cont=0
        if total==0:
            break


    