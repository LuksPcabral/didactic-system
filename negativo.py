maior = menor = valor = i = 0
print('Digite números inteiros! Um número menor que zero para o programa!')
while valor >= 0:
    valor = 2
    if valor > maior:
        maior = valor
    if (valor < menor) and (valor >= 0):
        menor = valor
    i += 1
print(maior)
print(menor)