# BEFORE CODE

# !/bin/python3

import math
import os
import random
import re
import sys


# CODING TASK


class Result:
    isMethodApplicable = True
    errorMessage = ""

    #
    # Complete the 'solveBySimpleIterations' function below.
    #
    # The function is expected to return a DOUBLE_ARRAY.
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. 2D_DOUBLE_ARRAY matrix
    #  3. DOUBLE epsilon
    #

    def solveBySimpleIterations(n, matrix, epsilon):
        # Write your code here

        # Split matrix into coefficients and constants
        coeff = [[0 for j in range(n)] for i in range(n)]
        const = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                coeff[i][j] = matrix[i][j]
            const[i] = matrix[i][n]

        # Check if matrix is diagonally dominant
        if not Result.checkDiagDomin(coeff):
            coeff = Result.sortingMatrixByRow(coeff)
            if not Result.checkDiagDomin(coeff):
                Result.isMethodApplicable = False
                Result.errorMessage = 'The system has no diagonal dominance for this method. Method of the ' \
                                      'simple iterations is not applicable. '

        # Use simple iterations method to get the result
        x = [0 for i in range(n)]
        x_new = [0 for i in range(n)]
        x = Result.simpleIterationMethod(coeff,const, x, x_new)
        return x

    # function to sort matrix
    def sortingMatrixByRow(coeff):

        for i in range(n):
            j_max = i
            for j in range(i, n - 1):
                if abs(coeff[i][j_max]) < abs(coeff[i][j + 1]):
                    j_max = j + 1
                if i != j_max:
                    for k in range(i, n):
                        coeff[k][i], coeff[k][j_max] = coeff[k][j_max], coeff[k][i]
        return coeff

    # function to check whether the diagonal element is larger than the sum
    def checkDiagDomin(coeff):
        n = len(coeff)
        for i in range(n):
            diag = abs(coeff[i][i])
            sum_row = 0
            for j in range(n):
                if i != j:
                    sum_row = sum_row + abs(coeff[i][j])
            if diag <= sum_row:
                return False
            else:
                return True

    # function to caculate the rusult with simlpe iteration method
    def simpleIterationMethod(coeff,const, x, x_new):
        n = len(coeff)
        while Result.isMethodApplicable:
            for i in range(n):
                sum = 0
                for j in range(n):
                    sum += coeff[i][j] * x[j]
                x_new[i] = x[i] - (sum - const[i]) / coeff[i][i]

            # Check whether difference is less then epsilon
            max_diff = 0
            for i in range(n):
                max_diff = max(max_diff, abs(x_new[i] - x[i]))
            if max_diff < epsilon:
                break
            #Update the X
            x = x_new.copy()

        return x


# AFTER CODE
if __name__ == '__main__':

    n = int(input().strip())

    matrix_rows = n
    matrix_columns = n + 1

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))

    epsilon = float(input().strip())
    # n = 2
    # matrix = [[1, 2, 3], [2, 1, 3]]
    # epsilon = 1
    result = Result.solveBySimpleIterations(n, matrix, epsilon)
    if Result.isMethodApplicable:
        print('\n'.join(map(str, result)))
    else:
        print(f"{Result.errorMessage}\n")
    print('\n')
