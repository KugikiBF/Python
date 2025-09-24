# n=1
# contpar=0
# contimpar=0
# while n!=0:
#     n= int(input("Digite um valor: "))
#     if n%2==0:
#         contpar+=1
#     else:
#         contimpar+=1
# print(F"voce digitou {contimpar} números impares")
# print(F"Voce digitou {contpar} números pares")





# sexo=str(input("Digite seu sexo[M/F]: ")).strip().upper()[0]
# while sexo not in "MmfF":
#     sexo=str(input("dados invalidos, tente novamente: ")).strip().upper()[0]
# print(f"sexo {sexo} registrado")



# from random import randint
# cont=0
# jogador=int(input("digite um numero: "))
# computador=randint(0,10)
# while jogador != computador:
#     jogador=int(input("Voce nao acertou,digite um numero: "))
#     cont+=1
#     if jogador==computador:
#         print("===="*21)
#         print(f"\033[32mVoce acertou eu escolhi o número {computador}, voce precisou de {cont} tentativas pra me derrotar\033[m")
#         print("===="*21)




# n1=int(input("digite um valor: "))
# n2=int(input("digite um valor: "))
# escolha=0
# while escolha !=5:
#     print(" [1]SOMAR")
#     print(" [2]MULTIPLICAR")
#     print(" [3]MAIOR")
#     print(" [4]NOVOS NÚMEROS")
#     print(" [5]SAIR")
#     escolha=int(input("Digite uma opção: "))
#     if escolha==1:
#         print(n1+n2)
#     if escolha==2:
#         print(n1*n2)
#     if escolha==3:
#         if n1>n2:
#             print(n1)
#         else:
#             print(n2)
#     if escolha==4:
#         n1=int(input("digite um valor: "))
#         n2=int(input("digite um valor: "))
#     if escolha==5:
#         print("Voce saiu")




# from math import factorial
# from time import sleep
# n=int(input("digite um numero: "))
# r= factorial(n)
# cont=n
# print(f"\033[34mCalculando {n}!  \033[m")
# sleep(1)
# while n >0:
#     print(F"{n}",end="")
#     print(f" X " if n>1 else f" = {r}",end="")
#     n-=1






# n1=int(input("Coloque o 1 termo: "))
# r=int(input("Coloque a razão: "))
# cont=1
# while cont != 10:
#     cont+=1
#     pa=(n1)+(cont*r)
#     print(pa)




# n1=int(input("Coloque o 1 termo: "))
# r=int(input("Coloque a razão: "))
# termo=n1
# cont=1
# total=0
# n=10
# while n !=0:
#     total=total+n
#     while cont <= total:
#         cont+=1
#         termo+=r
#         print(termo)
#     n=int(input("voce quer ver mais quantos termos? "))
#     if n==0:
#         print("ACABOU!")





# n=int(input("Quantos termos quer mostrar? "))
# t1=0
# t2=1
# print(F"{t1} --> {t2}",end="")
# cont=3
# while  cont<= n:
#     t3=t1+t2
#     print(F" --> {t3}",end="")
#     t1=t2
#     t2=t3
#     cont+=1
    



# cont=n=soma=0
# while n != 999:
#     n=int(input("digite um numero:"))
#     cont+=1
#     soma+=n
#     if n==999:
#         cont=cont-1
#         soma=soma-999
#         print("acabou")
# print(cont)
# print(soma)






p="a"
n=cont=maior=menor=soma=0
while p not in  "Nn":
    n=int(input("Digite um numero: "))
    soma+=n
    cont+=1
    m=soma/cont
    p=str(input("voce quer continuar?[S/N]: ")).strip().upper()[0]
    if cont ==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n

print(F"{cont}, {maior}, {menor}, {m} ")
        
   
    

