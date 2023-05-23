import copy
import pandas as pd


def triangular(entrada):
	saida = [None for x in range(len(entrada))]
	for i in reversed(range(0,len(entrada[0])-1)):
		soma = 0
		for j in reversed(range(i,len(entrada))):
			if i != j: 
				soma += saida[j]*entrada[i][j] 
			else: 
				saida[i]=(entrada[i][len(entrada[0])-1]-soma)/entrada[i][i] 
				break
	return saida

def escalonamento(entrada):
    n = len(entrada)
    anterior = copy.deepcopy(entrada)
    proximo = copy.deepcopy(entrada)
    iterations = []
    iterations.append(anterior)  # Armazena a matriz original como a primeira iteração
    for k in range(1, n):
        if proximo[k][k] == 0:
            return None
        anterior = copy.deepcopy(proximo)
        for i in range(n):
            for j in range(n+1):
                if i < k:
                    proximo[i][j] = anterior[i][j]
                elif i > k-1 and j < k:
                    proximo[i][j] = 0
                else:
                    proximo[i][j] = anterior[i][j] - (anterior[i][k-1] / anterior[k-1][k-1] * anterior[k-1][j])
        iterations.append(copy.deepcopy(proximo))  # Armazena cada iteração
    return iterations

def gauss(entrada):
    return triangular(escalonamento(entrada))

entrada = [[2, 0, 0, 0, 3], [1, 1.5, 0, 0, 4.5], [0, -3, 0.5, 0, -6.6], [2, -2, 1, 1, 0.8]]
iterations = gauss(entrada)

for i, iteration in enumerate(iterations):
    df = pd.DataFrame(iteration)
    print(f"Iteração {i+1}")
    print(df)
    print()