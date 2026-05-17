cadeiras = ['c1','c2','c3','c4','c5']
cadeiras_ocupadas = []          

for cadeira_p1 in cadeiras:
    for cadeira_p2 in cadeiras:
            if cadeira_p2 != cadeira_p1:
                for cadeira_p3 in cadeiras:
                    if cadeira_p3 != cadeira_p2 and cadeira_p3 != cadeira_p1:
                        cadeira_ocupada = cadeira_p1,cadeira_p2,cadeira_p3
                        cadeiras_ocupadas.append(cadeira_ocupada) 

colunas = 5

print(f"\nCadeiras ocupadas pelas 3 pessoas:  ")
for i, cadeira_ocupada in enumerate(cadeiras_ocupadas):
    print(f"{cadeira_ocupada}", end=",")
    if (i + 1) % colunas == 0:
        print()

if len(cadeiras_ocupadas) % colunas != 0:
    print()
    
print('Quantidade de maneiras de organizar as 3 pessoas: ', len(cadeiras_ocupadas))
