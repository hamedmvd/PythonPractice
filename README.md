# PythonPractice


type of Python Practice from assignments.these questions are so important for how want to become master in data structures. in addition that all of the practice accumulated in domain of tuple and list type.

> all of the solution are answered by me. so be careful that if you copy this, I promise that you can not be analyzing my Power in Python :)

# Practices

### Q 1
Complete the below function that takes two lists, constructs tuples with one element from each list and returns a list of the constructed tuples. For example,
```list_product(["a","b","c"], [1,2])``` returns 
```[("a",1), ("a",2), ("b",1), ("b",2), ("c",1), ("c",2)]```
If one of the lists is empty, then return an empty list. Note that the order of the lists are important in the construction of the tuples. Therefore, respect the order in the lists.




### A 1
```
def list_product(list1, list2):
	return [(i, j)for i in list2 for j in list1]
	
list_product(['a', 'b', 'c'], [1, 2])
```

### Q 2
Complete the below function which takes a list of distinct positive integers and a target positive integer value, and then returns a list of the pairs of integers where each pair sums up to the target value. Each pair is represented as a tuple. For example, 
```pairsum([3,2,6,1,5,4], 7)``` should return
```[(1,6), (2,5), (3,4)]```
If there are no pairs matching the target value, then you should return an empty list. IMPORTANT: the first integer in a tuple must be always smaller than the second integer. So, (5,3) is wrong and (3,5) is correct, and the resulting list must be in ascending order of first element in each tuple.




### A 2
```
def pairsum(list1, target):
	ans = []
	for j, b in enumerate(list1):
		for i, a in enumerate(list1[j:]):
			if a + b == 7:
				ans.append((a, b))
	return ans
print(pairsum([3,2,6,1,5,4], 7))
```

### Q 3
Complete the below function which takes the coefficients of a polynomial ```P(x)``` as a tuple, and a list of values, and returns a list of computed values of `P(x)`. Note that `P()` can be of any order. For example, 
```P((2,-1,1), [1,2,3])``` shall compute ```P(x)``` for ```x=1,2,3```
```P(x)=2x^2 -x +1```
where x^2 denotes the square of x. Hence, the function must return ```[2,7,16]```, because P(1) is 2, P(2) is 7, and P(3) is 16.




### A 3
```
def P(coefs,vals):
    if isinstance(coefs,list):
        coefs,vals=vals,coefs
    return [sum([x**i*c for i,c in enumerate(coefs[::-1])]) for x in vals]
    
print(P([1,2,3],(2,-1,1)))
```


### Q 4
Write a function that takes two dictionaries as arguments
and merges them into a new dictionary and returns this
new dictionary.

If the same key exists in both dictionaries, then the 
larger value is stored as the value of the key in the new dictionary. You can assume that all values are comparable.




### A 4
```
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
print(mergeDicts({'a':5, 'b':2, 'c':3}, {'f':2, 'H':1, 'a':1}))
```


