import numpy as np
from itertools import repeat


def nxn_matrix_solver(leftarr,rightarr):
    # initialize arrays
    left = np.array(leftarr)
    rightarray = np.array(rightarr)

    lenofcol = np.shape(left)[0]

    # initialize list to place determinants in
    variable = list(repeat(0, lenofcol))

    right = rightarray.T
    leftcopy = left.copy()
    determinant_arr =  np.linalg.det(left)

    # finding dx,dy,dz...
    for i in range((np.shape(left)[0])):
        temp = leftcopy[:,i]
        left[:,i] = right[:,0]
        variable[i] += np.linalg.det(left)
        left[:,i] = temp

    #printing results
    for i in range(len(variable)):
        variable_answer = round(variable[i]/determinant_arr)
        print('Variable ' + str(i + 1) + ' = ' + str(variable_answer))

nxn_matrix_solver([[1,2,1,-1],[3,2,4,4],[4,4,3,4],[2,0,1,5]],[[5,16,22,15]])
