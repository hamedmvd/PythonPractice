# PythonPractice


type of Python Practice from assignments.these questions are so important for how want to become master in data structures. in addition that all of the practice accumulated in domain of tuple and list type.

> all of the solution are answered by me. so be careful that if you copy this is promise that you can not be analyzing my Power in Python :)

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

