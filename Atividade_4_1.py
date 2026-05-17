estradas = ['A','B','C','D']
contagem = 0                 

print('Passeio' '(','Subida',',','Descida',')',':')

for subida in estradas:
    for descida in estradas:
        print('(',subida, ',',descida,')')
        contagem = contagem + 1  

print('Quantidade de passeios: ', contagem)
