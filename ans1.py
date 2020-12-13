def list_product(list1, list2):
	return [(i, j)for i in list2 for j in list1]
	
list_product(['a', 'b', 'c'], [1, 2])
