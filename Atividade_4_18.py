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
    
    
    
pessoas = ['A','B','C','D','E']

filas_obtidas = formar_filas(pessoas)
