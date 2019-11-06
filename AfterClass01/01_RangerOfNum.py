def solution(arr,sum):
	arr.sort()
	div = arr[len(arr)-1]-arr[0]
	if div>sum:
		return 1
	return 0

nums = int(input())
for x in range(nums):
	arr = list(map(int,input().split()))
	num = int(input())
	count=0
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			temp = solution([arr[x] for x in range(i,j+1)],num)
			if(temp==1):
				count+=1
	print(count)
