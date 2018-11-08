import math

entrada = input().split(" ")
A, B, C = entrada

maior = int((int(A) + int(B) + abs(int(A) - int (B))) / 2)
resultado = int((int(maior) + int(C) + abs(int(maior) - int (C))) / 2)

print('{} eh o maior'.format(resultado))