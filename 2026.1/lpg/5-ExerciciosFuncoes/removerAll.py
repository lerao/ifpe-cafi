def removeAll(lista, n):
  listaFinal = []
  for elem in lista:
    if elem != n:
      listaFinal.append(elem)
  if lista.count(n) > 0:
    resultado = "O " + str(n) + " removido " + str(lista.count(n))
  else:
    resultado = "Elemento não existe"
  return resultado

print(removeAll([1,2,2,2,3,4], 6))