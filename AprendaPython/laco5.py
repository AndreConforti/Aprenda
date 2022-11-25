# Faça um programa que leia três valores (A, B, C) e mostre-os na ordem lida.  Em seguida, mostre-os em ordem crescente e decrescente.

from smtpd import MailmanProxy

maior = 0
menor = 0
meio = 0

a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))

if b < a > c:
    maior = a
elif a < b > c:
    maior = b
else:
    maior = c

if b > a < c:
    menor = a
elif a > b < c:
    menor = b
else:
    menor = c

if (a == maior and b == menor) or (a == menor and b == maior): 
    meio = c
elif (b == maior and c == menor) or (b == menor and c == maior):
    meio = a
else: 
    meio = b


print(a, b, c)
print(maior, meio, menor)
print(menor, meio, maior)
