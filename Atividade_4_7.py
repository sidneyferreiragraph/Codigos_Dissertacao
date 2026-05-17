blusas = ['b1', 'b2', 'b3','b4','b5','b6','b7']
saias = ['s1', 's2','s3','s4','s5']

contagem = 0
print('Vestimentas: ')
for blusa in blusas:
    for saia in saias:
        print('(',blusa,',',saia,')')
        contagem = contagem + 1
print('Quantidade de vestimentas: ', contagem)
