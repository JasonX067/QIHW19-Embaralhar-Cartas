#J = VALETE
#Q = RAINHA
#K = REIS

import random

naipes = ['Ouro', 'Copas', 'Espadas', 'Paus']

numeros = ['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K' ]

cartas = []

#for para naipes
for i in range(4):

  #for para números
  for u in range(13):

    cartas.append(str(numeros[u])+" de "+naipes[i])
    
quantidades = int(input("fala quantas cartas você quer, viadão \n"))

random.shuffle(cartas)
for i in range(quantidades):
  print(cartas[i])
