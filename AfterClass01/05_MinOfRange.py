nums = int(input())
for x in range(nums):
	arr = list(map(int,input().split()))
	start,end = map(int,input().split())
	index = int(input())
	# helpArr = [arr[x] for x in range(start-1,end)]
	helpArr = arr[start-1:end]
	helpArr.sort()
	result = helpArr[index-1]
	print(result)