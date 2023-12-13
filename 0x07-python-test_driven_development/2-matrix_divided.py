#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""
def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.

    arg:

    matrix: a list of lists of integers or floats.
    div : The divisor number and must be integer or float.

    return:
        division sum

    raises:
        TypeError : matrix must be a matrix (list of lists) of integers/floats.
        TypeError : Each row of the matrix must have the same size.
        TypeError : div must be a number.
        ZeroDivisionError : division by zero.
    """
    result_list = []
    for l in  matrix:
        sub_result_list = []
        if not all(len(row) == len(matrix[0]) for row in matrix):
          raise TypeError("Each row of the matrix must have the same size")
        else:
            for i in l:
                if not isinstance(i, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                elif not isinstance(div, (int,float)):
                    raise TypeError("div must be a number")
                elif div == 0:
                    raise ZeroDivisionError("division by zero")
                else:
                    result = round (i / div, 2)
                    sub_result_list.append(result)
            result_list.append(sub_result_list)

    return(result_list)
        