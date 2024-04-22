def raiz_quadrada(n):
  # Inicializa a base b com 2
  b = 2
  # Calcula p usando a fórmula p = (b + n / b) / 2
  p = (b + n / b) / 2
  # Repete enquanto a diferença absoluta entre b e p for maior que 0.0001
  while abs(b - p) > 0.0001:
    # Atualiza b com o valor de p
    b = p
    # Recalcula p usando a fórmula p = (b + n / b) / 2
    p = (b + n / b) / 2
  # Retorna o valor de p como a raiz quadrada aproximada de n
  return p

# Solicita ao usuário que digite um número
n = float(input("Digite um número: "))
# Chama a função raiz_quadrada com o número digitado e armazena o resultado em r
r = raiz_quadrada(n)
# Exibe o resultado na tela com duas casas decimais
print(f"A raiz quadrada de {n} é aproximadamente {r:.2f}")