entrada_segundos = int(input())
val = entrada_segundos
horas = minutos = segundos = 0

if int(entrada_segundos/3600) >= 1:
    horas = int(entrada_segundos/3600)
    entrada_segundos -= horas * 3600

if int(entrada_segundos/60) >= 1:
    minutos = int(entrada_segundos/60)
    entrada_segundos -= minutos * 60

if int(entrada_segundos/1) >= 1:
    segundos = int(entrada_segundos/1)
    entrada_segundos -= segundos * 1

print('{}:{}:{}'.format(horas, minutos, segundos))