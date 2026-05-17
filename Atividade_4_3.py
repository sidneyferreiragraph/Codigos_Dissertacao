moeda = ['CARA','COROA']
contagem = 0                  

print('Resultados',':  '  )

for lancamento1 in moeda:
    for lancamento2 in moeda:
        for lancamento3 in moeda:
            print('(',lancamento1, ',',lancamento2, ',', lancamento3,')')
            contagem = contagem + 1  

print('Quantidade de sequências: ', contagem)
