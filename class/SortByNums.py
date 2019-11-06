def relative(arr1,arr2):
# 	arr2 += sorted(set(arr1) - set(arr2))
# 	arr1.sort(key=arr2.index)
# 	return arr1
	diff = [a for a in arr1 if a not in arr2]
	diff = sorted(diff)
	res = []
	for a in arr2:
		res += [a for _ in range(arr1.count(a))]
	res += diff
	return res


nums = int(input())
for x in range(nums):
	one,two = map(int,input().split())
	arr1 = list(map(int,input().split()))
	arr2 = list(map(int,input().split()))
	arr = relative(arr1,arr2)
	print(arr)

