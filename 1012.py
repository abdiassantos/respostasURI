entrada = input().split(" ")
pi = float(3.14159)

A, B, C = entrada

area_triangulo = (float(A) * float(C))/2
area_circulo = pi * (float(C)**2)
area_trapezio = ((float(A) + float(B)) * float(C)) /2
area_quadrado = float(B) * float(B)
area_retangulo = float(A) * float(B)

print('TRIANGULO: {:.3f}'.format(area_triangulo))
print('CIRCULO: {:.3f}'.format(area_circulo))
print('TRAPEZIO: {:.3f}'.format(area_trapezio))
print('QUADRADO: {:.3f}'.format(area_quadrado))
print('RETANGULO: {:.3f}'.format(area_retangulo))