def transpose(matrix):
    new_matrix = matrix[:]
    count1 = len(matrix)
    count2 = len(matrix[0])
    matrix.clear()
    for j in range(count2):
        a = []
        for i in range(count1):
            a = a + [new_matrix[i][j]]
        matrix.append(a)
    return matrix
