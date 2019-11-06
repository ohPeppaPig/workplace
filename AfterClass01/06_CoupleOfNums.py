def solution(arr,target):
	start = 0
	end = len(arr)-1
	count = 0
	while start<end:
		sum = arr[start]+arr[end]
		if target>sum:
			start+=1
		elif target<sum:
			end-=1
		else:
			count+=1
			start+=1
			end+=1
	return count
nums = int(input())
for x in range(nums):
	arr = list(map(int,input().split()))
	target = int(input())
	arr.sort()
	result = solution(arr,target)
	print(result)



