tempo_gasto = int(input())
velocidade_media = int(input())

espaco_percorrido = tempo_gasto * velocidade_media

litros_necessarios = espaco_percorrido / 12

print('{:.3f}'.format(litros_necessarios))