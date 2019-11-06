num = int(input())
for x in range(num):
	arr = list(map(int,input().split()))
	w = int(input())
	result = 0
	for i in range(0,len(arr)-w+1):
		# helpArr = [arr[x] for x in range(i,i+w)]
		helpArr = arr[i:i+w]
		result+=max(helpArr)
	print(result)