def triangleOrNot(a, b, c):
    len1 = len(c)
    result = [None]*len1
    for x in range(len1):
        z = (a[x] + b[x] + c[x])/2
        if(z <= a[x] or z <= b[x] or z <= c[x]):
            result[x] = 'No'
        else:
            result[x] = 'Yes'
    return result;
