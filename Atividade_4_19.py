def formar_filas(pessoas):

    print("\n" + "=" * 60)
    print("PASSO 1: Forma as filas.")
    print("=" * 60)
    
    resultado = []
    contador_filas = 0

    for pessoa_1 in pessoas:
        for pessoa_2 in pessoas:
            if pessoa_2 != pessoa_1:
                for pessoa_3 in pessoas:
                    if pessoa_3 != pessoa_2 and pessoa_3 != pessoa_1:
                        contador_filas += 1
                        fila_formada = [pessoa_1,pessoa_2,pessoa_3]
                        resultado.append(fila_formada)
                        print(f"Fila {contador_filas:3d}: {fila_formada}")

    print(f"\nTotal de filas diferentes: {contador_filas}")
    return resultado    
 
def ordenar_e_imprimir_filas(filas):
    
    print("\n" + "=" * 60)
    print("PASSO 2: Ordena cada fila individualmente")
    print("=" * 60)
    
    filas_ordenadas = []
    ordenadas = []
    
    print("\nTodas as filas ORDENADAS:")
    print("-" * 60)
       
    for idx, fila in enumerate(filas, 1):
        fila_ordenada = sorted(fila)
        filas_ordenadas.append(fila_ordenada)
        print(f"Fila {idx}: {fila_ordenada}")
        
    return filas_ordenadas
    
def remover_duplicatas_sort(lista):
    
    print("\n" + "=" * 60)
    print("PASSO 3: Coloca as filas iguais em uma mesma caixa")
    print("=" * 60)
    
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
    print("Número de filas: ", len(lista_ordenada))
    print()
    print("Depois que as filas são ordenadas, temos: ", len(grupo_atual) , " filas em cada caixa.")
    print()
        
    resultado = [lista_ordenada[0]]
    
    for i in range(1, len(lista_ordenada)):
        if lista_ordenada[i] != lista_ordenada[i-1]:
            resultado.append(lista_ordenada[i])
    return resultado

    
pessoas = ['A','B','C','D','E']

filas_obtidas = formar_filas(pessoas)
ordenadas = ordenar_e_imprimir_filas(filas_obtidas)
grupos = remover_duplicatas_sort(ordenadas)

print("Todas os grupos:")
for i, perm in enumerate(grupos, 1):
    print(f"{i:3}. {perm}")
print(f"Número de grupos: {len(grupos)}")
