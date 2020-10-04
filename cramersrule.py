def determinant(array):
    if len(array) == 2:
        return (array[0][0] * array[1][1]) - (array[0][1] * array[1][0])
    else:
        a = array[0][0]
        b = array[0][1]
        c = array[0][2]
        ax =  a * ((array[1][1] * array[2][2]) - (array[1][2] * array[2][1]))
        ab = b * ((array[1][0] * array[2][2]) - (array[2][0] * array[1][2]))
        ac = c * ((array[1][0] * array[2][1]) - (array[2][0] * array[1][1]))
        return (ax - ab) + ac

def makedeterminant(arr):
    copyarr = []
    variable = []
    for i in range(len(arr)):
        y = arr[i].pop(len(arr[i])-1)
        variable.append(y)
    copyofarr = copy.deepcopy(arr)
    copyofarr2 = copy.deepcopy(arr)
    copyofarr3 = copy.deepcopy(arr)
    d = determinant(arr)
    dx = copyofarr.copy()
    values = iter(variable)
    for i in range(len(arr)):
        dx[i][0] = next(values)
    dxx = determinant(dx)
    dy = copyofarr2
    values2 = iter(variable)
    for i in range(len(arr)):
        dy[i][1] = next(values2)
    dyy = determinant(dy)
    if len(arr[0]) == 2:
        return 'x = ' + str(dxx/d) + ' y = ' + str(dyy/d)
    dz = copyofarr3
    values3 = iter(variable)
    for i in range(len(arr)):
        dz[i][2] = next(values3)
    dzz = determinant(dz)
    return 'x = ' + str(dxx/d) + ' y = ' + str(dyy/d) + ' z = ' + str(dzz/d)




print(makedeterminant([[12,3,15],[2,-3,13]]))
