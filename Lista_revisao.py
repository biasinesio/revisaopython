"""Construa um programa para cada questão apresentada abaixo que abrange os conceitos e estruturas
trabalhas em Python, são elas: os operadores matemáticos, estruturas condicionais, estruturas de
repetição, variáveis e vetores."""


'''1. Faça um programa que calcule a média de três números inseridos pelo usuário.'''

from asyncio.format_helpers import _format_callback_source
from urllib.request import FancyURLopener


n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
n3 = float(input("Digite a sua terceira nota: "))
media = (n1 + n2 + n3)/3
print ("Sua média é:", media)


'''2. Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.'''

numero = int(input("Escreva um número: "))
if numero % 2 == 0:
 print(f"O número {numero} é par.")
else:
 print(f"O número {numero} é ímpar.")

'''3. Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
esse número.'''

numero = int(input("Escreva um número: "))

print (f"Números pares de 0 até {numero}")
for i in range (0, numero + 1 , 2 ):
 print (i)

'''4. Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.'''
lista_numeros = [0,1,2,3,6,5,4,9,8,7,10,86,54,79,72,16,54]

if len (lista_numeros) > 0:
 maximo = minimo = lista_numeros[0]
maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)

print (lista_numeros) 
print (f"O maior número da lista é: {maior_valor}")
print (f"O menor número da lista é: {menor_valor}")

'''5. Faça um programa que leia uma lista de números e retorne a média dos números pares.'''
numeros = input("Digite uma lista de números separados por espaço: ")

lista_numeros = [int(numero) for numero in numeros.split()]
soma_pares = 0
quantidade_pares = 0

for numero in lista_numeros :
    if numero % 2 == 0:
      soma_pares += numero
      quantidade_pares += 1

if quantidade_pares > 0:
  media_pares = soma_pares / quantidade_pares
  print(f"A média dos números pares é: {media_pares:.2f}")
else:
  print("Não foram encontrados números pares na lista.")

'''6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse
número.'''

def calcular_fatorial(numero):
  if numero == 0 or numero == 1:
    return 1
  else:
    return numero * calcular_fatorial(numero - 1)
  
try:
  numero = int(input("Digite um número inteiro positivo: "))
  if numero < 0:
    print("Por favor, digite um número positivo. ")
  else:
    fatorial = calcular_fatorial(numero)
    print(f"O fatorial do {numero} é {fatorial}: ")
except ValueError:
  print("Entrada inválida. Por favor, digite um número inteiro positivo.")



'''7. Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.'''
def fibonacci(limite):
  sequencia = [0, 1]
  while sequencia[-1] + sequencia [-2] <= limite:
      prox_num = sequencia[-1] + sequencia [-2]
      sequencia.append(prox_num)
  return sequencia

valor_inserido = int(input("Insira um valor limite para a sequ~encia de Fibonacci: "))
resultado_sequencia = fibonacci(valor_inserido)
print ("Sequência de Fibonacci até", valor_inserido,":",resultado_sequencia)


'''8. Faça um programa que determine se um número é primo ou não.'''

def primo (numero):
  if numero <= 1:
    return False
  if numero <= 3:
    return True
  if numero % 2 == 0 or numero % 3 == 0:
    return False
  
  i=5
  while i * i <= numero:
    if numero % i <= numero:
      if numero % i == 0 or numero % (i + 2) == 0:
        return False
      i += 6
      return True

num = int(input("Digite um número: "))
if primo(num):
  print (f"{num} é uma número Primo!")
else:
  print (f"{num} Não é um número Primo!")


'''9. Escreva um programa que leia uma lista de nomses e retorne uma nova lista com apenas os nomes que
começam com a letra 'A'.'''
def filtrar_nomes_por_letra(nomes, letra):
  nomes_filtrados = [nome for nome in nomes if nome.startswith(letra)]
  return nomes_filtrados
lista_de_nomes = ["Ana", "Leandro", "Marcos", "Amanda", "Beatriz", "Carlos", "Arthur"]

letra_incial = "A"
nomes_com_a = filtrar_nomes_por_letra(lista_de_nomes, letra_incial)
print ("Lista de nomes:", lista_de_nomes)
print ("Nomes comecando por A:", nomes_com_a)


'''10. Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O
programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do
computador e determinar o vencedor.'''

import random 

def jogo_pedra_papel_tesoura(escolha_usuario):
  escolhas = ["Pedra", "Papel","Tesoura"]
  escolha_computador = random.choice(escolhas)

  print (f"O computador escolheu: {escolha_computador}")

  if escolha_usuario == escolha_computador:
    resultado = "Empate"

  elif (escolha_usuario =="Pedra") and (escolha_computador == "Tesoura") or \
       (escolha_usuario =="Papel") and (escolha_computador == "Pedra") or \
       (escolha_usuario =="Tesoura") and (escolha_computador == "Papel"):
    resultado ="Você ganhou!"

  else:
    resultado = "Computador venceu!"

  print (resultado)

escolha_usuario = input("Escolha Pedra, Papel ou Tesoura: ")
jogo_pedra_papel_tesoura(escolha_usuario=escolha_usuario)