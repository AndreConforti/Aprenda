# Faça um programa que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 + … + 1/n.

num = int(input('Digite i, valor positivo: '))
soma = 0
for i in range(1, num + 1):
    soma += 1/i

print(soma)
