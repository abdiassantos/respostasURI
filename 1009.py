nome = str(input())
salario_fixo = round(float(input()), 2)
salario_vendas = round(float(input()), 2)

vendas = salario_vendas * 0.15
TOTAL = vendas + salario_fixo

print('TOTAL = R$ {:.2f}'.format(TOTAL))