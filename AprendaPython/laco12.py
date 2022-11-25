# Escreva um programa que lê o tamanho do lado de um quadrado e imprime um quadrado daquele tamanho com asteriscos. Seu programa deve usar laços de repetição e funcionar para quadrados com lados de todos os tamanhos entre 1 e 20.

# x = -3

lado = int(input('Informe o lado do quadrado: '))
print()

# for l in range(lado):
#     x = x + 1

for l in range(lado):    
    if l == 0 or l == (lado -1):
        print('* ' * (lado))
    else:
        print('*', ' ' * (lado + 2), '*')




