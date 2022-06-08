def flippingMatrix(matrix):
    n_matrix_teste = int(len(matrix)/2)

    def somar():
        soma =0
        for i in range(0, n_matrix_teste):
            for j in range(0, n_matrix_teste):
                soma = soma + matrix[i][j]
        return soma
    return somar()


print(flippingMatrix([[1,2], [3, 4]]))