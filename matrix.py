"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ""
    for i in range(4):
        for point in matrix:
            s = s + str(point[i]) + " "
        s = s + "\n"
    print(s)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    side = len(matrix)
    for i in range(side):
        matrix[i][i] = 1
    for r in range(side):
        for c in range(side):
            if r !=c :
                matrix[r][c] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for r in range(len(m2)):
        m2[r] = multi_helper(m1, m2[r])

def multi_helper(m1, m2 ):
    final = []
    for i in range(len(m1)):
        sum = 0
        for c in range(len(m1[i])):
            sum = sum + (m1[i][c] * m2[c])
        final.append(sum)
    return final


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
