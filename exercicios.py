# -*- coding: utf-8 -*-
"""Exercicios

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qRKhY7J9aVzwfLx_tUuhnvqiVJZXl-hU
"""

from random import randrange, sample

lista =  []
for i in range (0,20):
   lista.append(randrange(100))

sample(lista, 5)

import math

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")

!pip install matplotlib==3.7.1

import numpy as np

from random import choices

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
resultado = choices(lista)
print(resultado)

from random import randrange

num = randrange(100)
print(num)

from math import pow

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

result = pow(n1,n2)

print(f"A potencia do número {n1} elevado ao número {n2} é igual a {result}" )

from random import randrange
n_participantes = int(input('Digite o total de participantes do sorteio: '))

sorteio = randrange(n_participantes)

print(f'O número sorteado é: {sorteio}')

from random import randint

nome = input('Olá, usuário! Digite seu nome:')

num = randint(1000, 9998)

while num % 2 != 0:
  num = randint(1000, 9998)

else:
  token = num
  print(f"Olá, {nome}, o seu token de acesso é {token}!")

from random import choices
frutas = ["maçã", "banana", "uva", "pêra",
         "manga", "coco", "melancia", "mamão",
        "laranja", "abacaxi", "kiwi", "ameixa"]

salada = choices(frutas, k = 3)
print(salada)

from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

for i in numeros:
  raiz = sqrt(i)

  if raiz.is_integer():
    print(f"O a raiz de {i} é {raiz:.2f} e é inteira.")
  else:
    print(f"O a raiz de {i} é {raiz:.2f} e não é inteira.")

from math import pow
pi = 3
raio = float(input("Digite o raio do circulo:"))
area = pi*pow(raio, 2)
print(f"A area da grama vale {area*25}m2")