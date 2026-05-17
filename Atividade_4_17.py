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


def remover_duplicatas_sort(lista):
        
    lista_ordenada = sorted(lista) 
  
    lista_de_listas = []
    grupo_atual = []
    for i in range(len(lista_ordenada)):
        if i == 0 or lista_ordenada[i] == lista_ordenada[i - 1]:
            grupo_atual.append(lista_ordenada[i])
        else:
            lista_de_listas.append(grupo_atual)
            grupo_atual = [lista_ordenada[i]]
    lista_de_listas.append(grupo_atual)
    
    for i, uplas in enumerate(lista_de_listas, 1):
        print(f"{i:3}. {uplas}")
    print()
    print("Número de anagramas: ", len(lista_ordenada))
    print()
    print("Número de anagramas repetidos em cada caixa: ", len(grupo_atual))
    print()
    
    
    resultado = [lista_ordenada[0]]

    for i in range(1, len(lista_ordenada)):
        if lista_ordenada[i] != lista_ordenada[i-1]:
            resultado.append(lista_ordenada[i])
    return resultado

palavra = str(input("Digite uma palavra qualquer: ")).upper()

todas_permutacoes = permutacoes(palavra)
permutacoes_com_elemetos_repetidos = remover_duplicatas_sort(todas_permutacoes)


print(f"\nAnagramas da palavra {palavra}: ")
for i, perm in enumerate(permutacoes_com_elemetos_repetidos, 1):
    print(f"{i:3}. {perm}")
print(f"Quantidade de anagramas da palavra {palavra}: {len(permutacoes_com_elemetos_repetidos)}")














