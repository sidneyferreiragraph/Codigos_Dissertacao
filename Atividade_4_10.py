algarismos = [0,1,2,3,4,5,6,7,8,9]
contagem = 0                  

print('Números pares formados: ')
for unidades in algarismos:
    if unidades % 2 == 0:
        for dezenas in algarismos:
            if dezenas != 0 and dezenas != unidades:
                print(dezenas,unidades)
                contagem = contagem + 1  

print('Quantidade de números pares com dois algarismos distintos: ', contagem)
