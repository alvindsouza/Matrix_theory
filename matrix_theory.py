import time
import numpy as np

a  =  np.array( [[1,2,3],
        [4,5,6],
        [7,8,9]])
b = np.array(  [
        [9,8,7],
        [6,5,4],
        [3,2,1]])
A = np.array([[2,1],
             [7,4]])
B = np.array([[4,-1],
             [-7,2]])
b = a 
def A_plus_b(matrix_a, matrix_b):
    mat = matrix_a.copy()
    if len(mat) == len(matrix_b) and len(mat[0]) == len(matrix_b[0]):

        for col in range(len(mat[0])):
            c = []
            for index,row in enumerate(mat): 
                row[col] += matrix_b[index][col]

        return mat
    else:
        print('the matrices are of diffenent size')
def scalar_prod(matrix, multi): 
    mat = [row[:] for row in matrix] 
    for row in mat: 
        for col in range(len(row)): 
            row[col] *= multi 
    return mat

def transpose (matrix):

    transposed= []
    for col in range(len(matrix[0])):
        c = []
        for row in  a: 
            c.append(row[col])
        transposed.append(c)
    # for i in transposed:
    #         for el in i:
    #             print (el,end= ' ')
    #         print()    
    return transposed
def multiply (matrix_a, matrix_b):
    if len(matrix_a[0]) == len(transpose(matrix_b)):
        product = []
        for row_a in a:
            p_row= []
            for row_b in transpose(b):
                element = 0 
                for i in range(len(row_a)):
                    # print(f'{row_a[i]}*{row_b[i]}')
                    element += row_a[i]*row_b[i]
                p_row.append(element)    
                # print('-----')
            product.append(p_row)        

    else:
        print('no of rows in matrix a is not equal to no of columns in matrix b')

    return np.array(product)
def print_matrix(matrix):
    for i in matrix:
            for el in i:
                print (el,end= ' ')
            print()
def A_minus_b(matrix_a, matrix_b):
    mat = matrix_a.copy()
    if len(mat) == len(matrix_b) and len(mat[0]) == len(matrix_b[0]):

        for col in range(len(mat[0])):
            c = []
            for index,row in enumerate(mat): 
                row[col] -= matrix_b[index][col]
        return mat
    else:
        print('the matrices are of diffenent size')
def check_symmetric(matrix) :
    if matrix== transpose(matrix):
        return True
    else:
        return False
def identity(matrix):
    print('To prove')
    print("A = 1/2( A + A') + 1/2 ( A - A' )")
    print('-------------------------------------------------------')
    # time.sleep(5)
    print_matrix(matrix)
    print('=')
    print('1/2(')
    print_matrix(matrix)
    print('+')
    print_matrix(transpose(matrix))
    print(')')
    print('+')
    print('1/2(')
    print_matrix(matrix)
    print('-')
    print_matrix(transpose(matrix))
    print(')')
    print('-------------------------------------------------------')
    # time.sleep(2)
    print_matrix(matrix)
    print('+')
    print_matrix(transpose(matrix))
    print('=')
    print_matrix(A_plus_b(matrix,transpose(matrix)))
    # time.sleep(2)
    print('1/2(')
    print_matrix(A_plus_b(matrix,transpose(matrix)))
    print(')')
    print('=')
    print_matrix(A_plus_b(matrix,transpose(matrix))*1//2)

    print('-------------------------------------------------------')
    # time.sleep(2)
    print_matrix(matrix)
    print('-')
    print_matrix(transpose(matrix))
    print('=')
    print_matrix(A_minus_b(matrix,transpose(matrix)))
    print('-------------------------------------------------------')
# identity(a)

def inverse(matrix_a,matrix_b):
    if len(matrix_a) == len(matrix_a[0]) and len(matrix_b) == len(matrix_b[0]) :
        print_matrix(matrix_a)
        print('x')
        print_matrix(matrix_b)
        print('=')
        print_matrix(multiply(matrix_a,matrix_b))
        print('-------------')        
        pass
        print_matrix(matrix_b)
        print('x')
        print_matrix(matrix_a)
        print('=')
        print_matrix(multiply(matrix_b,matrix_a))
        print('-------------')        
        identity_matrix =np.zeros((len(matrix_a[0]),len(matrix_a[0])))
        np.fill_diagonal(identity_matrix, 1)

        if np.array_equal(multiply(matrix_b,matrix_a),multiply(matrix_a,matrix_b),identity_matrix):
            print('=')
            print_matrix(identity_matrix)
            print('Inverse - Positive')
def find_adjoint(matrix):
    mat = [row[:] for row in matrix] 
    mat[0][0],mat[1][1] = mat[1][1],mat[0][0]
    mat[0][1]*=-1
    mat[1][0]*=-1
    return mat
print_matrix(find_adjoint(A))