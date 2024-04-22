apagar = 0
while True:
    código = int(input("Código da mercadoria (0 para sair): "))
    preço = 0
    if código == 0:
        break
    elif código == 1:
        preço = 5.50
    elif código == 2:
        preço = 2.30
    elif código == 3:
        preço = 4.75
    elif código == 5:
        preço = 6.80
    elif código == 9:
        preço = 9.30
    else:
        print("Código inválido!")
    if preço != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preço * quantidade)
print(f"Total a pagar R${apagar:8.2f}")
