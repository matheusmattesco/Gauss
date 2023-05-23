import streamlit as st
import pandas as pd
import copy


def gauss(entrada):
    def triangular(entrada):
        n = len(entrada)
        saida = [None] * n

        for i in reversed(range(n)):
            soma = 0
            for j in range(i + 1, n):
                soma += saida[j] * entrada[i][j]
            saida[i] = (entrada[i][n] - soma) / entrada[i][i]

        return saida

    def escalonamento(entrada):
        n = len(entrada)

        for k in range(n - 1):
            if entrada[k][k] == 0:
                return None

            for i in range(k + 1, n):
                fator = entrada[i][k] / entrada[k][k]
                for j in range(k, n + 1):
                    entrada[i][j] -= fator * entrada[k][j]

        return entrada

    return triangular(escalonamento(entrada))

calculo = [[2, 7, 6, 8, 9, 8], 
           [1, 1.5, 0, 6, 4.5, 8], 
           [0, -3, 0.5, 0, -9, 8], 
           [0, -2, 9, 3, 8, 8]]

st.write("Matriz Antes do Calculo")
data = calculo
df = pd.DataFrame(data)

st.dataframe(df)




saida = gauss(calculo)

st.write("Matriz Apos o Calculo")
data = calculo
df = pd.DataFrame(data)

st.dataframe(df)


st.write("Resultado do Método de Eliminação de Gauss:")
df_saida = pd.DataFrame(saida)
st.dataframe(df_saida)
