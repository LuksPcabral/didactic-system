paisA = 70000

paisB = 180000

qtdAnos = 0

while paisB > paisA :

 populacaoPaisA = paisA * 0.03

 populacaoPaisB = paisB * 0.015

 paisA = paisA + populacaoPaisA

 paisB = paisB + populacaoPaisB

 qtdAnos = qtdAnos + 1

print("O país A passará o país B em" ,qtdAnos, "anos")