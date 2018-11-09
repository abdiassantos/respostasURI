entrada = input().split(" ")
A, B, C = entrada

delta = (float(B)**2) - (4 * float(A) * float(C))

if (float(delta) >= 0) and (float(A) is not 0.0):
    X1 = (((-1)*float(B)) + (float(delta)**(1/2))) / (2*float(A))
    X2 = (((-1)*float(B)) - (float(delta)**(1/2))) / (2*float(A))
    print('R1 = {:.5f}'.format(X1))
    print('R2 = {:.5f}'.format(X2))
else:
    print('Impossivel calcular')