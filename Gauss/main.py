import streamlit as st
from gauss import gauss
from gaussseidel import seidel

def main():
    st.title("Resolução de Sistemas Lineares")
    st.header("Método de Gauss-Seidel e Eliminação de Gauss")

    st.subheader("Entrada")
    st.write("Digite a matriz A:")
    A = create_matrix_input("A", [[5, 1, 1], [3, 4, 1], [3, 3, 6]])
    st.write("Digite o vetor b:")
    b = create_vector_input("b", [5, 6, 0])
    epsilon = st.number_input("Epsilon", value=0.05, step=0.01)

    st.subheader("Resultado")
    if st.button("Resolver usando Gauss-Seidel"):
        result_gs = seidel(A, b, epsilon)
        st.write("Resultado usando Gauss-Seidel:")
        st.write(result_gs)

    if st.button("Resolver usando Eliminação de Gauss"):
        result_gauss = gauss(A, b)
        st.write("Resultado usando Eliminação de Gauss:")
        st.write(result_gauss)

def create_matrix_input(name, default_value):
    matrix = []
    for i, row in enumerate(default_value):
        matrix_row = []
        for j, value in enumerate(row):
            value = st.number_input(f"{name}[{i}][{j}]", value=value)
            matrix_row.append(value)
        matrix.append(matrix_row)
    return matrix

def create_vector_input(name, default_value):
    vector = []
    for i, value in enumerate(default_value):
        value = st.number_input(f"{name}[{i}]", value=value)
        vector.append(value)
    return vector


if __name__ == "__main__":
    main()