import random

r = random.randint(1,100)
tentativas = 0
while True:
    tentativa_usuario = int(input("Adivinhe o número secreto entre 1 e 100: "))
    tentativas += 1
    if tentativa_usuario > r:
        print("Tente um número menor.")
    elif tentativa_usuario < r:
        print("Tente um número maior.")
    else:
        print(f"Parabéns! Você adivinhou corretamente em {tentativas} tentativas.")
        break