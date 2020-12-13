def pairsum(list1, target):
	ans = []
	for j, b in enumerate(list1):
		for i, a in enumerate(list1[j:]):
			if a + b == 7:
				ans.append((a, b))
	return ans
pairsum([3,2,6,1,5,4], 7)
