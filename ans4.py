def mergeDicts(a,b):
    resp = {}
    for i in a.keys()|b.keys():
        if i in a and i in b:
            resp[i]=max(a[i],b[i])
        elif i in b:
            resp[i]=b[i]
        else:
            resp[i]=a[i]
    return resp
mergeDicts({'a':5, 'b':2, 'c':3}, {'f':2, 'H':1, 'a':1})
