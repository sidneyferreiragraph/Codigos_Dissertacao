letras = ['M','O','S','T','R','A']
vogais = ['A','O']
consoantes = ['M','R','S','T']
anagramas = []

for letra_1 in letras:
    if letra_1 in vogais:
        for letra_6 in letras:
            if letra_6 in consoantes:
                for letra_2 in letras:
                    if letra_2 != letra_1 and letra_2 != letra_6:
                        for letra_3 in letras:
                            if letra_3 != letra_2 and letra_3 != letra_1 and letra_3 != letra_6:
                                for letra_4 in letras:
                                    if letra_4 != letra_3 and letra_4 != letra_2 and letra_4 != letra_1 and letra_4 != letra_6:
                                        for letra_5 in letras:
                                            if letra_5 != letra_4 and letra_5 != letra_3 and letra_5 != letra_2 and letra_5 != letra_1 and letra_5 != letra_6:
                                                anagrama = (letra_1 + letra_2 + letra_3 + letra_4 + letra_5 + letra_6)
                                                anagramas.append(anagrama)

colunas = 12

print(f"\nAnagramas da palavra MOSTRA que começam por vogal e teminam por consoante: ")
for i, anagrama in enumerate(anagramas):
    print(f"{anagrama},", end="")
    if (i + 1) % colunas == 0:
        print()

if len(anagramas) % colunas != 0:
    print()
    
print('Quantidade de anagramas: ', len(anagramas))
