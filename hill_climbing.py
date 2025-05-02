import random
import time

# Matriz de custos (Empresa × Projeto)
matriz_custos = [
    [12, 18, 15, 22, 9, 14, 20, 11, 17],
    [19, 8, 13, 25, 16, 10, 7, 21, 24],
    [6, 14, 27, 10, 12, 19, 23, 16, 8],
    [17, 11, 20, 9, 18, 13, 25, 14, 22],
    [10, 23, 16, 14, 7, 21, 12, 19, 15],
    [13, 25, 9, 17, 11, 8, 16, 22, 20],
    [21, 16, 24, 12, 20, 15, 9, 18, 10],
    [8, 19, 11, 16, 22, 17, 14, 10, 13],
    [15, 10, 18, 21, 13, 12, 22, 9, 16]
]



# Função para calcular o custo total de uma solução
def calcular_custo(solucao):
    return sum(matriz_custos[i][solucao[i]] for i in range(9))

# Função para gerar vizinhos trocando dois projetos entre empresas
def gerar_vizinhos(solucao):
    vizinhos = []
    for i in range(9):
        for j in range(i+1, 9):
            vizinho = solucao[:]
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            vizinhos.append(vizinho)
    return vizinhos

# Algoritmo de Hill Climbing
def subida_encosta():
    inicio = time.time()
    atual = list(range(9))
    random.shuffle(atual)
    custo_atual = calcular_custo(atual)
    
    while time.time() - inicio < 15:  # Limite de 15 segundos
        vizinhos = gerar_vizinhos(atual)
        melhor_vizinho = min(vizinhos, key=calcular_custo)
        melhor_custo = calcular_custo(melhor_vizinho)

        if melhor_custo < custo_atual:
            atual = melhor_vizinho
            custo_atual = melhor_custo
        else:
            break  # Nenhuma melhoria encontrada

    tempo_total = time.time() - inicio
    return atual, custo_atual, tempo_total

# Executar o algoritmo
solucao, custo_total, tempo_execucao = subida_encosta()
print("Solução encontrada (empresa -> projeto):", solucao)
print("Custo total da solução:", custo_total)
print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
