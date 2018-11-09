value = float(input())

cem = cinquenta = vinte = dez = cinco = dois = um = 0
cincents = vintecincents = dezcents = cincocents = cents = 0

value = float('{:.2f}'.format(value))
if int(value/100) >= 1:
	cem = int(value/100)
	value -= cem*100

value = float('{:.2f}'.format(value))
if int(value/50) >= 1:
	cinquenta = int(value/50)
	value -= cinquenta*50

value = float('{:.2f}'.format(value))
if int(value/20) >= 1:
	vinte = int(value/20.00)
	value -= vinte*20

value = float('{:.2f}'.format(value))
if int(value/10) >= 1:
	dez = int(value/10)
	value -= dez*10.00

value = float('{:.2f}'.format(value))
if int(value/5) >= 1:
	cinco = int(value/5)
	value -= cinco*5

value = float('{:.2f}'.format(value))
if int(value/2) >= 1:
	dois = int(value/2)
	value -= dois*2

value = float('{:.2f}'.format(value))
if int(value/1) >= 1:
	um = int(value/1)
	value -= um*1

value = float('{:.2f}'.format(value))
if int(value/0.50) >= 1:
	cincents = int(value/0.50)
	value -= cincents*0.50

value = float('{:.2f}'.format(value))
if int(value/0.25) >= 1:
	vintecincents = int(value/0.25)
	value -= vintecincents*0.25

value = float('{:.2f}'.format(value))
if int(value/0.10) >= 1:
	dezcents = int(value/0.10)
	value -= dezcents*0.10

value = float('{:.2f}'.format(value))
if int(value/0.05) >= 1:
	cincocents = int(value/0.05)
	value -= cincocents*0.05

value = float('{:.2f}'.format(value))
if int(value/0.01) >= 0.998:
	cents = int(value/0.01)
	value -= cents*0.01

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(cem))
print('{} nota(s) de R$ 50.00'.format(cinquenta))
print('{} nota(s) de R$ 20.00'.format(vinte))
print('{} nota(s) de R$ 10.00'.format(dez))
print('{} nota(s) de R$ 5.00'.format(cinco))
print('{} nota(s) de R$ 2.00'.format(dois))

print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(um))
print('{} moeda(s) de R$ 0.50'.format(cincents))
print('{} moeda(s) de R$ 0.25'.format(vintecincents))
print('{} moeda(s) de R$ 0.10'.format(dezcents))
print('{} moeda(s) de R$ 0.05'.format(cincocents))
print('{} moeda(s) de R$ 0.01'.format(cents))