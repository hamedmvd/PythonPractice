def P(coefs,vals):
    if isinstance(coefs,list):
        coefs,vals=vals,coefs
    return [sum([x**i*c for i,c in enumerate(coefs[::-1])]) for x in vals]
    
P([1,2,3],(2,-1,1))
