def substituicoes_retroativas(A, b):
    n = len(A)
    
    x = n * [0] 
    
    for i in range(n-1, -1, -1):
        S = 0
        for j in range(i+1, n):
            S = S + A[i][j] * x[j]
        x[i] = (b[i] - S)/A[i][i]

    return x

def gauss(A, b):
    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            m = - A[i][k]/A[k][k]
            for j in range(k+1, n):
                A[i][j] = m * A[k][j] + A[i][j]
            b[i] = m * b[k] + b[i]
            A[i][k] = 0

    x = substituicoes_retroativas(A, b)
    return x