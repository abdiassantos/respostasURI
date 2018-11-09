entrada = input().split(" ")
A, B, C, D = entrada

if (int(B) > int(C)) and (int(D) > int(A)):
    if (int(C) + int(D)) > (int(A) + int(B)):
        if int(C) >= 0 and int(D) >= 0:
            if int(A)%2 == 0:
                print('Valores aceitos')
            else:
                print('Valores nao aceitos')
        else:
            print('Valores nao aceitos')
    else:
        print('Valores nao aceitos')    
else:
    print('Valores nao aceitos')