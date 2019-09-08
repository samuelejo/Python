import math
from Utils import cmDebug as cm


def nonlin(x, deriv = False):
    R = list()
    if deriv:
        for item in x:
            R.append(item * (1 - item))
    else:
        for item in x:
            R.append( 1 / (1 + math.exp(-item)) )

    return R

def clean(M):
    try:
        len(M[0])
        return M[0]
    except IndexError:
        return M
    except TypeError:
        return M

def transpose(M):
    if M == []:
        cm ('Matrix M is empty', 'fail')
        return []

    rows = len(M)
    try:
        cols = len(M[0])
    except TypeError:
        cols = 1
    

    # Transpose M
    T = list()
    for col in range (cols):
        A = list()
        for row in range (rows):
            if rows == 1 and cols == 1:
                M = clean(M)
                A.append(M[0])
            elif rows != 1 and cols == 1:
                A.append(M[row])
            else:
                A.append(M[row][col])
        
        if len(A) == 1:
            T.append(A[0])
        else:
            T.append(A)
    return T

def add(A, B):
    if not isinstance(A, list) or not isinstance(B, list):
        cm ('Either matrix A or B is not a matrix', 'fail')
        return []
    if A == [] or B == []:
        cm ('Either matrix A or B is empty', 'fail')
        return []
    
    try:
        rowsA = len(A)
        rowsB = len(B)
        colsA = len(A[0])
        colsB = len(B[0])
    except TypeError:
        try:
            rowsA += 0
        except UnboundLocalError:
            rowsA = 1
        try:
            colsA += 0
        except UnboundLocalError:
            colsA = 1
        try:
            rowsB += 0
        except UnboundLocalError:
            rowsB = 1
        try:
            colsB += 0
        except UnboundLocalError:
            colsB = 1
    if rowsA != rowsB or colsA != colsB:
        cm ("Matrix A is not of the same order as matrix B", 'fail')
        return []
    
    # Add B to A
    Sum = list()
    for row in range (rowsA):
        Row = list()
        for col in range (colsA):
            if rowsA != 1 and colsA != 1:
                Row.append(A[row][col] + B[row][col])
            elif rowsA != 1 and colsA == 1:
                Row.append(A[row] + B[row])
            elif rowsA == 1 and colsA != 1:
                Row.append(A[0][col] + B[0][col])
            elif rowsA == 1 and colsA == 1:
                A = clean(A)
                B = clean(B)
                Row.append(A[0] + B[0])
        
        if len(Row) == 1:
            Sum.append(Row[0])
        else:
            Sum.append(Row)
    return Sum

def mult(A, k):
    if not isinstance(A, list) or not (isinstance(k, int) or isinstance(k, float)):
        cm ('Either matrix A is not a matrix or k a number', 'fail')
        return []
    if A == []:
        cm ('Matrix A is empty', 'fail')
        return []
    
    rowsA = len(A)
    try:
        colsA = len(A[0])
    except TypeError:
        colsA = 1
    
    # Multiply A by k
    Mul = list()
    for row in range (rowsA):
        Row = list()
        for col in range (colsA):
            if colsA != 1:
                Row.append(k * A[row][col])
            else:
                Row.append(k * A[row])
        if len(Row) == 1:        
            Mul.append(Row[0])
        else:        
            Mul.append(Row)
    return Mul

def multMatrix(A, B):
    if not isinstance(A, list) or not isinstance(B, list):
        cm ('Either matrix A or B is not a matrix', 'fail')
        return []
    if A == [] or B == []:
        cm ('Either matrix A or B is empty', 'fail')
        return []
    
    rowsA = len(A)
    rowsB = len(B)
    try:
        colsA = len(A[0])
    except TypeError:
        colsA = 1
    try:
        colsB = len(B[0])
    except TypeError:
        colsB = 1
    if rowsA != rowsB or colsA != colsB:
        cm ("Matrix A is not of the same order as matrix B", 'fail')
        return []
    
    # Add B to A
    Mult = list()
    for row in range (rowsA):
        Row = list()
        for col in range (colsA):
            if rowsA != 1 and colsA != 1:
                Row.append(A[row][col] * B[row][col])
            elif rowsA != 1 and colsA == 1:
                Row.append(A[row] * B[row])
            elif rowsA == 1 and colsA != 1:
                Row.append(A[0][col] * B[0][col])
            elif rowsA == 1 and colsA == 1:
                A = clean(A)
                B = clean(B)
                Row.append(A[0] * B[0])
        
        if len(Row) == 1:
            Mult.append(Row[0])
        else:
            Mult.append(Row)
    return Mult

def dot(A, B, t1 = False, t2 = False):
    if not isinstance(A, list) or not isinstance(B, list):
        cm ('Either matrix A or B is not a matrix', 'fail')
        return []
    if A == [] or B == []:
        cm ('Either matrix A or B is empty', 'fail')
        return []
        
    if t1:
        A = transpose(A)
    if t2:
        B = transpose(B)

    rowsA = len(A)
    rowsB = len(B)
    try:
        colsA = len(A[0])
    except TypeError:
        colsA = 1
    try:
        colsB = len(B[0])
    except TypeError:
        colsB = 1

    if colsA != rowsB:
        cm ("Cols of A does not equal rows of B", 'fail')
        return []

    dotM = list()

    for row in range (rowsA):
        R = list()
        for c in range (colsB):
            sum = 0
            for r in range (rowsB):
                if colsB != 1:
                    if rowsA != 1 and colsA != 1:
                        sum += A[row][r] * B[r][c]
                    elif rowsA != 1 and colsA == 1:
                        sum += A[row] * B[0][c]
                    elif rowsA == 1 and colsA != 1:
                        sum += A[0][r] * B[r][c]
                    elif rowsA == 1 and colsA == 1:
                        A = clean(A)
                        B = clean(B)
                        sum += A[0] * B[0][c]
                if colsB == 1:
                    if rowsA != 1 and colsA != 1:
                        sum += A[row][r] * B[r]
                    elif rowsA != 1 and colsA == 1:
                        sum += A[row] * B[0]
                    elif rowsA == 1 and colsA != 1:
                        sum += A[0][r] * B[r]
                    elif rowsA == 1 and colsA == 1:
                        A = clean(A)
                        B = clean(B)
                        sum += A[0] * B[0]
                
            R.append(sum)
        
        if len(R) == 1:
            dotM.append(R[0])
        else:
            dotM.append(R)
    return (dotM)


############################################

if __name__ == "__main__":
    
    pass