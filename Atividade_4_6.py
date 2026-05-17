algarismos = [0,1,2,3,4,5,6,7,8,9]
contagem = 0                  

print('Números formados: ')
for dezenas in algarismos:
    if dezenas != 0:
        for unidades in algarismos:
            if unidades != dezenas:
                print(dezenas,unidades)
                contagem = contagem + 1  

print('Quantidade de números com dois algarismos distintos: ', contagem)

