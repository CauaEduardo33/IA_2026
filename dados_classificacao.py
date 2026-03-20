import math # Trazendo a matemática para o Python

# 1. A NOSSA BASE DE DADOS (Dataset)
# Formato: [Peso (gramas), Tamanho (cm), "Nome da Fruta"]
dados_frutas = [
    [150, 8.0, "Maçã"],
    [160, 9.0, "Maçã"],
    [145, 7.5, "Maçã"],
    [20,  3.0, "Morango"],
    [22,  3.5, "Morango"],
    [18,  2.8, "Morango"],
    [131, 6.0, "Laranja"],
    [147, 7.3, "Laranja"],
    [160, 8.0, "Laranja"]
]

# 2. A FÓRMULA DE DISTÂNCIA (Teorema de Pitágoras)
def calcular_distancia(x1, y1, x2, y2):
    # Distância = Raiz Quadrada de ((x2 - x1)² + (y2 - y1)²)
    conta = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    return math.sqrt(conta)

# 3. O CÉREBRO DA NOSSA IA
def classificar_fruta(novo_peso, novo_tamanho, base_de_dados):
    menor_distancia = 999999.0 # Começamos com um número gigante
    melhor_resposta = ""

    # A IA vai "olhar" para cada fruta que ela já conhece na lista
    for fruta in base_de_dados:
        peso_conhecido = fruta[0]
        tamanho_conhecido = fruta[1]
        nome_conhecido = fruta[2]

        # Calcula a distância geométrica entre a fruta nova e a conhecida
        dist = calcular_distancia(novo_peso, novo_tamanho, peso_conhecido, tamanho_conhecido)
        print(f"Distância para {nome_conhecido}: {dist:.2f}\n")        


        # Se essa distância for a menor que já vimos, atualizamos a resposta!
        if dist < menor_distancia:
            menor_distancia = dist
            melhor_resposta = nome_conhecido


    return melhor_resposta

# --- TESTANDO A IA ---
print("--- IA DE CLASSIFICAÇÃO GEOMÉTRICA ---")
peso_misterioso = float(input("Digite o peso da fruta misteriosa (g): "))
tamanho_misterioso = float(input("Digite o tamanho da fruta misteriosa (cm): "))

resultado = classificar_fruta(peso_misterioso, tamanho_misterioso, dados_frutas)
print(f"\n=> Pela distância matemática, a IA deduziu que é um(a): {resultado}!")