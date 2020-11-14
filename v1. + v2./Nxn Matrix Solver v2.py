import numpy as np
from itertools import repeat


def nxn_matrix_solver(leftarr,rightarr):
    # initialize arrays
    leftarr = np.array(leftarr)
    rightarr = np.array(rightarr)
    
    # initialize list to place determinants in
    variables = list(repeat(0, lenofcol))
    
    lenofcol = np.shape(leftarr)[0]
    vector_col = rightarr.T
    leftcopy = leftarr.copy()
    determinant_arr =  np.linalg.det(leftarr)

    # finding dx,dy,dz...
    for i in range((np.shape(leftarr)[0])):
        temp = leftcopy[:,i]
        leftarr[:,i] = vector_col[:,0]
        variables[i] += np.linalg.det(leftarr)
        leftarr[:,i] = temp

    #printing results
    for i in range(len(variables)):
        variable_answer = round(variables[i]/determinant_arr)
        print('Variable ' + str(i + 1) + ' = ' + str(variable_answer))

nxn_matrix_solver([[1,2,1,-1],[3,2,4,4],[4,4,3,4],[2,0,1,5]],[[5,16,22,15]])
