import copy as copy

def determinant(array):
    # if it is a 2x2 matrix
    if len(array) == 2:
        return (array[0][0] * array[1][1]) - (array[0][1] * array[1][0])
    # if it is a 3x3 matrix
    else:
        a = array[0][0]
        b = array[0][1]
        c = array[0][2]
        ax =  a * ((array[1][1] * array[2][2]) - (array[1][2] * array[2][1]))
        ab = b * ((array[1][0] * array[2][2]) - (array[2][0] * array[1][2]))
        ac = c * ((array[1][0] * array[2][1]) - (array[2][0] * array[1][1]))
        return (ax - ab) + ac

def cramers_rule(arr):
    # making copies for each determinant and gettind rid of last column
    copyarr = []
    variable = []
    for i in range(len(arr)):
        y = arr[i].pop(len(arr[i])-1)
        variable.append(y)
    copyofarr =  copy.deepcopy(arr)
    copyofarr2 = copy.deepcopy(arr)
    copyofarr3 = copy.deepcopy(arr)
    
    # calculating dx 
    d = determinant(arr)
    d1 = copyofarr
    for i in range(len(arr)):
        d1[i][0] = variable[i]
    dx = determinant(d1)
    
    #calculating dy
    d2 = copyofarr2
    for i in range(len(arr)):
        d2[i][1] = variable[i]
    dy = determinant(d2)
    
    # check if it is a 2x2 matrix
    if len(arr[0]) == 2:
        return 'x = ' + str(dx/d) + ' y = ' + str(dy/d)
    
    # calculating dz
    d3 = copyofarr3
    for i in range(len(arr)):
        d3[i][2] = variable[i]
    dz = determinant(d3)
    
    return 'x = ' + str(dx/d) + ' y = ' + str(dy/d) + ' z = ' + str(dz/d)




print(cramers_rule([[12,3,15],[2,-3,13]]))
