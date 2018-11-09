entrada_dias = int(input())
guardar_dias = entrada_dias
ano = mes = dia = 0

if int(entrada_dias/365) >= 1:
    ano = int(entrada_dias/365)
    entrada_dias -= ano * 365

if int(entrada_dias/30) >= 1:
    mes = int(entrada_dias/30)
    entrada_dias -= mes * 30

if int(entrada_dias/1) >= 1:
    dia = int(entrada_dias/1)
    entrada_dias -= dia * 1

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))