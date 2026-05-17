cores = ['amarelo','rosa', 'verde']
contagem = 0                  

for cor1 in cores:
    for cor2 in cores:
        if cor2 != cor1:
            for cor3 in cores:
                if cor3 != cor2:
                    for cor4 in cores:
                        if cor4 != cor3:
                            print('(',cor1, ',',cor2, ',', cor3, ',', cor4,')')
                            contagem = contagem + 1  

print('Quantidade de maneiras de colorir a bandeira: ', contagem)
