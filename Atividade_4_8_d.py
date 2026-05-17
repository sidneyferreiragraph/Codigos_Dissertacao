import string

alfabeto = list(string.ascii_uppercase)
palavras = []


for letra1 in alfabeto:
    for letra2 in alfabeto:
        if letra2 != letra1:
            palavra = letra1 + letra2
            palavras.append(palavra)
        
        
colunas = 26

print(f"\nPalavras formadas:  ")
for i, palavra in enumerate(palavras):
    print(f"{palavra}", end=",")
    # Adiciona uma quebra de linha a cada 'colunas' números
    if (i + 1) % colunas == 0:
        print()

# Adiciona uma quebra de linha final, se necessário
if len(palavras) % colunas != 0:
    print()
    
print('Quantidade de palavras formadas: ', len(palavras))
