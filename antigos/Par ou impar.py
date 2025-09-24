from random import choice
from random import randint
cont=0
print("=-"*20)
print("vamos jogar par ou impar".upper())
print("=-"*20)
while True:
    n=int(input("Digite um valor: "))
    j=(input("Escolha par ou ímpar[P/I] ".upper()).upper()).upper()[0]
    print("-"*40)
    comp=randint(0,10)
    soma=n+comp
    if soma%2==0 and j=="P":
        cont+=1
        print(F"Voce jogou {n} e o computador {comp}. Total de {soma} deu par")
        print("-"*40)
        print("voce ganhou".upper())
        print("Vamos jogar novamente...")
        print("=-"*20)
    if soma%2!=0 and j=="I":
        cont+=1
        print(F"Voce jogou {n} e o computador {comp}. Total de {soma} deu impar")
        print("-"*40)
        print("voce ganhou".upper())
        print("Vamos jogar novamente...")
        print("=-"*20)
    if soma%2==0 and j=="I":
        print(f"GAME OVER! Voce venceu {cont} vezes.")
        break
    if soma%2!=0 and j=="P":
        print(f"GAME OVER! Voce venceu {cont} vezes.")
        break