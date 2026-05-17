def permutacoes(palavra):
    if len(palavra) == 1:
        return [palavra]
    
    resultado = []
    
    for i in range(len(palavra)):
        char_atual = palavra[i]
        resto = palavra[:i] + palavra[i+1:]
        for p in permutacoes(resto):
            resultado.append(char_atual + p)
    
    return resultado

palavra = 'NUMERO'

todas_permutacoes = permutacoes(palavra)

colunas = 20

print(f"\nAnagramas da palavra NÚMERO: ")
for i, anagrama in enumerate(todas_permutacoes):
    print(f"{anagrama},", end="")
    if (i + 1) % colunas == 0:
        print()

if len(todas_permutacoes) % colunas != 0:
    print()
    
print('Quantidade de anagramas: ', len(todas_permutacoes))


