import math # Trazendo a matemática para o Python

# 1. A NOSSA BASE DE DADOS (Dataset)
# Formato: [Peso (toneladas), Tamanho (L), "Nome da Fruta"]
dados_veiculos = [
  [1.5, 1.0, "carro"],
  [1.7, 1.5, "carro"],
  [1.9, 2.0, "carro"],
  [0.1, 0.125, "moto"],
  [0.175, 0.3, "moto"],
  [0.25, 0.6, "moto"],
  [6.0, 7.0, "caminhão"],
  [14.5, 10.0, "caminhão"],
  [23.0, 13.0, "caminhão"]
]

# 2. A FÓRMULA DE DISTÂNCIA (Teorema de Pitágoras)
def calcular_distancia(x1, y1, x2, y2):
    # Distância = Raiz Quadrada de ((x2 - x1)² + (y2 - y1)²)
    conta = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    return math.sqrt(conta)

# 3. O CÉREBRO DA NOSSA IA
def classificar_veiculo(novo_peso, novo_tamanho, base_de_dados):
    menor_distancia = 999999.0 # Começamos com um número gigante
    melhor_resposta = ""

    # A IA vai "olhar" para cada veículo que ela já conhece na lista
    for veiculo in base_de_dados:
        peso_conhecido = veiculo[0]
        tamanho_conhecido = veiculo[1]
        nome_conhecido = veiculo[2]

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
peso_misterioso = float(input("Digite o peso do veículo (toneladas): "))
tamanho_misterioso = float(input("Digite o tamanho do motor (L): "))

resultado = classificar_veiculo(peso_misterioso, tamanho_misterioso, dados_veiculos)
print(f"\n=> Pela distância matemática, a IA deduziu que é um(a): {resultado}!")