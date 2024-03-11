# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int:
    # TU CÓDIGO AQUÍ
    is_square = len(matrix) == len(matrix[0])
    sum_diagonal = 0

    if is_square:
        for i in range(len(matrix)):
            sum_diagonal += matrix[i][i]
    else:
        sum_diagonal = None


    return sum_diagonal


if __name__ == '__main__':
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])